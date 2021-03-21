from backend.server import server
from backend.relationDB.models import db
from flask import request, abort, jsonify
from backend.queueMessaging.consumers.changeMessageConsumer import ChangeMessageConsumer
from backend.queueMessaging.messageHandlers.CUDMessageHandler import CUDMessageHandler

from backend.documentDB.repositories.categoryRepositoryDocumentDB import CategoryRepositoryDocumentDB
from backend.documentDB.repositories.productRepositoryDocumentDB import ProductRepositoryDocumentDB

from backend.relationDB.repositories.categoryRepository import create_new_category, get_category_by_id, update_category, delete_category, \
                                                               get_all_root_category, get_children_category

from backend.relationDB.repositories.productRepository import create_new_product, get_product_by_id, update_product, delete_product,\
                                                              get_products_by_category_id


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


#####################################################################################################
# ============================================USER==================================================#
#####################################################################################################

# -------------------------------------------category------------------------------------------------

@server.route("/catalog/category", methods=['GET'])
def catalog_category_get():
    try:
        category_id = request.args.get("category_id")
        category = CategoryRepositoryDocumentDB.get_category_by_id(int(category_id))
        return jsonify(category)
    except():
        abort(400)


@server.route("/catalog/category/roots", methods=['GET'])
def catalog_get_root_categories():
    try:
        root_categories = CategoryRepositoryDocumentDB.get_all_root_category()
        return jsonify([root_categories])
    except():
        abort(400)


@server.route("/catalog/category/children", methods=['GET'])
def catalog_get_children_categories():
    try:
        category_id = request.args.get("category_id")
        children_categories = CategoryRepositoryDocumentDB.get_all_children_category(int(category_id))
        return jsonify([children_categories])
    except():
        abort(400)

# -------------------------------------------product------------------------------------------------

@server.route("/catalog/product", methods=['GET'])
def catalog_product_get():
    try:
        product_id = request.args.get("product_id")
        product = ProductRepositoryDocumentDB.get_product_by_id(int(product_id))
        return jsonify(product)
    except():
        abort(400)


@server.route("/catalog/products", methods=['GET'])
def catalog_products_get():
    try:
        category_id = request.args.get("category_id")
        products = ProductRepositoryDocumentDB.get_products_by_category_id(int(category_id))
        return jsonify([products])
    except():
        abort(400)


#####################################################################################################
# ============================================ADMIN=================================================#
#####################################################################################################

# -------------------------------------------category------------------------------------------------

@server.route("/admin/category", methods=['POST'])
def admin_category_post():
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
    except():
        abort(400)


@server.route("/admin/category", methods=['GET'])
def admin_category_get():
    try:
        category_id = request.args.get("category_id")
        category = get_category_by_id(category_id)
        return category.serialize()
    except():
        abort(400)


@server.route("/admin/category", methods=['PUT'])
def admin_category_put():
    try:
        message = request.get_json()

        category_id = message["category_id"]
        category_name = message["category_name"]
        root_category_id = message["root_category_id"]

        update_category(category_id, category_name, root_category_id)
        return "succ"
    except():
        abort(400)


@server.route("/admin/category", methods=['DELETE'])
def admin_category_delete():
    try:
        category_id = request.args.get("category_id")
        delete_category(category_id)
        return "succ"
    except():
        abort(400)


@server.route("/admin/category/roots", methods=['GET'])
def admin_get_root_categories():
    try:
        root_categories = get_all_root_category()
        return jsonify([e.serialize() for e in root_categories])
    except():
        abort(400)


@server.route("/admin/category/children", methods=['GET'])
def admin_get_children_categories():
    try:
        category_id = request.args.get("category_id")
        children_categories = get_children_category(category_id)
        return jsonify([e.serialize() for e in children_categories])
    except():
        abort(400)


# -------------------------------------------product------------------------------------------------


@server.route("/admin/product", methods=['POST'])
def admin_product_post():
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


@server.route("/admin/product", methods=['GET'])
def admin_product_get():
    try:
        product_id = request.args.get("product_id")
        product = get_product_by_id(product_id)
        return product.serialize()
    except():
        abort(400)


@server.route("/admin/products", methods=['GET'])
def admin_products_get():
    try:
        category_id = request.args.get("category_id")
        products = get_products_by_category_id(category_id)
        return jsonify([e.serialize() for e in products])
    except():
        abort(400)


@server.route("/admin/product", methods=['PUT'])
def admin_product_put():
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


@server.route("/admin/product", methods=['DELETE'])
def admin_product_delete():
    try:
        product_id = request.args.get("product_id")
        delete_product(product_id)
        return "succ"
    except():
        abort(400)



if __name__ == "__main__":
    db.create_all()
    changeMessageConsumer = ChangeMessageConsumer(CUDMessageHandler())
    changeMessageConsumer.start_consuming_thread()
    server.run(host='0.0.0.0', port=5000)
