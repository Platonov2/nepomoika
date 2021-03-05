from server import server
from models import db
from flask import request, abort, jsonify
from repositories.categoryRepository import create_new_category, get_category_by_id, update_category, delete_category, get_all_root_category,\
                                            get_children_category

from repositories.productRepository import create_new_product, get_product_by_id, update_product, delete_product


@server.route("/")
def root():
    return """
    Hi stranger. It's me, agricultural store UwU
                                                       
               ..-::*************::-...             
         .-:****+%@###############@%+****:-.        
      .***=@##@%+*******************+%@###=***:.    
      :*##+********++***#+****************+%##**.   
     -*%#*******+%+**#%*%#*******************#@*-   
    .**#=********=###@####*******************+#=*.  
    -*%#**************+@####=*****************@@*-  
    :*#%*********@######@*********************=#**  
   .*=#+************%###+**********************#=*. 
   .*%#************=####***********@=**********#%*. 
   -*%#************######+*********+##*********#%*- 
   .*%#*********+=@##################+*********#%*. 
   .*=#****=##########################*********#=*. 
   .*+#+*****@#+***+%########@@#######@*******+#+*. 
    :*#%*******%#=***************%#####=******%#*:  
    -*%#*********+@#****************+@####=***#%*.  
    .:*#%*********************************##+%#*:.  
     .*=#+*********************************=##+*.   
      -*+%##@=***************************=@##=*-    
        .-***+%@####@%=++*****++=%@####@%+***-.     
             ..-:******+=======+******:-..          
                        .......                     
                                 
    """


# -------------------------------------------category------------------------------------------------

@server.route("/category", methods=['POST'])
def category_post():
    # """
    # Display the home page.
    #
    # **Context**
    #
    # ``user_projects``
    #     Active :model:`reporting.ProjectAssignment` for current :model:`users.User`
    # ``upcoming_projects``
    #     Future :model:`reporting.ProjectAssignment` for current :model:`users.User`
    # ``recent_tasks``
    #     Five most recent :model:`django_q.Task` entries
    # ``user_tasks``
    #     Incomplete :model:`reporting.ReportFindingLink` for current :model:`users.User`
    #
    # **Template**
    #
    # :template:`index.html`
    # """
    try:
        message = request.get_json()[0]
        category_name = message["category_name"]
        root_category_id = int(message["root_category_id"])

        create_new_category(category_name, root_category_id)
        return "succ"
        # return message
    except():
        abort(400)


@server.route("/category", methods=['GET'])
def category_get():
    try:
        category_id = request.args.get("category_id")
        category = get_category_by_id(category_id)
        return category.serialize()
    except():
        abort(400)


@server.route("/category", methods=['PUT'])
def category_put():
    try:
        message = request.get_json()

        category_id = message["category_id"]
        category_name = message["category_name"]
        root_category_id = message["root_category_id"]

        update_category(category_id, category_name, root_category_id)
        return "succ"
    except():
        abort(400)


@server.route("/category", methods=['DELETE'])
def category_delete():
    try:
        category_id = request.args.get("category_id")
        delete_category(category_id)
        return "succ"
    except():
        abort(400)


@server.route("/category/roots", methods=['GET'])
def get_root_categories():
    try:
        root_categories = get_all_root_category()
        return jsonify([e.serialize() for e in root_categories])
    except():
        abort(400)


@server.route("/category/children", methods=['GET'])
def get_children_categories():
    try:
        category_id = request.args.get("category_id")
        children_categories = get_children_category(category_id)
        return jsonify([e.serialize() for e in children_categories])
    except():
        abort(400)


# -------------------------------------------product------------------------------------------------


@server.route("/product", methods=['POST'])
def product_post():
    try:
        message = request.get_json()[0]
        product_name = message["product_name"]
        product_price = message["product_price"]
        image_link = message["image_link"]
        product_category_id = message["product_category_id"]
        create_new_product(product_name, product_price, image_link, product_category_id)
        return "succ"
    except():
        abort(400)


@server.route("/product", methods=['GET'])
def product_get():
    try:
        product_id = request.args.get("product_id")
        product = get_product_by_id(product_id)
        return product.serialize()
    except():
        abort(400)


@server.route("/product", methods=['PUT'])
def product_put():
    try:
        message = request.get_json()
        product_id = message["product_id"]
        product_name = message["product_name"]
        product_price = message["product_price"]
        image_link = message["image_link"]
        product_category_id = message["product_category_id"]
        update_product(product_id, product_name, product_price, image_link, product_category_id)
        return "succ"
    except():
        abort(400)


@server.route("/product", methods=['DELETE'])
def product_delete():
    try:
        product_id = request.args.get("product_id")
        delete_product(product_id)
        return "succ"
    except():
        abort(400)


if __name__ == "__main__":
    db.create_all()
    server.run(host='0.0.0.0', port=5000)
