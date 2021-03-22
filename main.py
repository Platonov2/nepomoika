from backend.server import server
from backend.relationDB.models import db
from flask import request, abort, jsonify
from backend.queueMessaging.consumers.changeMessageConsumer import ChangeMessageConsumer
from backend.queueMessaging.messageHandlers.CUDMessageHandler import CUDMessageHandler

from backend.documentDB.repositories.categoryRepositoryDocumentDB import CategoryRepositoryDocumentDB
from backend.documentDB.repositories.productRepositoryDocumentDB import ProductRepositoryDocumentDB

from backend.relationDB.repositories.categoryRepositoryRelationDB import CategoryRepositoryRelationDB
from backend.relationDB.repositories.productRepositoryRelationDB import ProductRepositoryRelationDB


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
    category_id = request.args.get("category_id", None)
    if category_id:
        category = CategoryRepositoryDocumentDB.get_category_by_id(int(category_id))
        return jsonify(category)
    else:
        return jsonify({"msg": "bad request"}), 400


@server.route("/catalog/category/roots", methods=['GET'])
def catalog_get_root_categories():
    root_categories = CategoryRepositoryDocumentDB.get_all_root_category()
    return jsonify(root_categories)


@server.route("/catalog/category/children", methods=['GET'])
def catalog_get_children_categories():
    category_id = request.args.get("category_id", None)
    if category_id:
        children_categories = CategoryRepositoryDocumentDB.get_all_children_category(int(category_id))
        return jsonify(children_categories)
    else:
        return jsonify({"msg": "bad request"}), 400


# -------------------------------------------product------------------------------------------------


@server.route("/catalog/product", methods=['GET'])
def catalog_product_get():
    product_id = request.args.get("product_id", None)
    if product_id:
        product = ProductRepositoryDocumentDB.get_product_by_id(int(product_id))
        return jsonify(product)
    else:
        return jsonify({"msg": "bad request"}), 400


@server.route("/catalog/products", methods=['GET'])
def catalog_products_get():
    category_id = request.args.get("category_id", None)
    if category_id:
        products = ProductRepositoryDocumentDB.get_products_by_category_id(int(category_id))
        return jsonify(products)
    else:
        return jsonify({"msg": "bad request"}), 400


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
    message = request.json[0]  # TODO странный формат json
    category_name = message["category_name"]
    root_category_id = message["root_category_id"]
    if category_name and root_category_id:
        CategoryRepositoryRelationDB.create_new_category(category_name, int(root_category_id))
        return "succ", 200
    else:
        return jsonify({"msg": "bad request json"}), 400


@server.route("/admin/category", methods=['GET'])
def admin_category_get():
    category_id = request.args.get("category_id", None)
    if category_id:
        category = CategoryRepositoryRelationDB.get_category_by_id(category_id)
        return category.serialize()
    else:
        return jsonify({"msg": "bad request"}), 400


@server.route("/admin/category", methods=['PUT'])
def admin_category_put():
    category_id = request.json.get("category_id", None)
    category_name = request.json.get("category_name", None)
    root_category_id = request.json.get("root_category_id", None)
    if category_id and category_name:
        CategoryRepositoryRelationDB.update_category(category_id, category_name, root_category_id)
        return "succ", 200
    else:
        return jsonify({"msg": "bad request json"}), 400


@server.route("/admin/category", methods=['DELETE'])
def admin_category_delete():
    category_id = request.args.get("category_id", None)
    if category_id:
        CategoryRepositoryRelationDB.delete_category(category_id)
        return "succ", 200
    else:
        return jsonify({"msg": "bad request"}), 400


@server.route("/admin/category/roots", methods=['GET'])
def admin_get_root_categories():
    root_categories = CategoryRepositoryRelationDB.get_all_root_category()
    return jsonify([e.serialize() for e in root_categories])


@server.route("/admin/category/children", methods=['GET'])
def admin_get_children_categories():
    category_id = request.args.get("category_id", None)
    if category_id:
        children_categories = CategoryRepositoryRelationDB.get_children_category(category_id)
        return jsonify([e.serialize() for e in children_categories])
    else:
        return jsonify({"msg": "bad request"}), 400


# -------------------------------------------product------------------------------------------------


@server.route("/admin/product", methods=['POST'])
def admin_product_post():
    message = request.get_json()[0]
    product_name = message["product_name"]
    product_price = message["product_price"]
    image_link = message["image_link"]
    product_category_id = message["product_category_id"]
    if product_name and product_price and image_link and product_category_id:
        ProductRepositoryRelationDB.create_new_product(product_name, product_price, image_link, product_category_id)
        return "succ", 200
    else:
        return jsonify({"msg": "bad request json"}), 400


@server.route("/admin/product", methods=['GET'])
def admin_product_get():
    product_id = request.args.get("product_id", None)
    if product_id:
        product = ProductRepositoryRelationDB.get_product_by_id(product_id)
        return product.serialize()
    else:
        return jsonify({"msg": "bad request"}), 400


@server.route("/admin/products", methods=['GET'])
def admin_products_get():
    category_id = request.args.get("category_id", None)
    if category_id:
        products = ProductRepositoryRelationDB.get_products_by_category_id(category_id)
        return jsonify([e.serialize() for e in products])
    else:
        return jsonify({"msg": "bad request"}), 400


@server.route("/admin/product", methods=['PUT'])
def admin_product_put():
    product_id = request.json.get("product_id", None)
    product_name = request.json.get("product_name", None)
    product_price = request.json.get("product_price", None)
    image_link = request.json.get("image_link", None)
    product_category_id = request.json.get("product_category_id", None)
    if product_id and product_name and product_price and image_link and product_category_id:
        ProductRepositoryRelationDB.update_product(product_id, product_name, product_price, image_link, product_category_id)
        return "succ", 200
    else:
        return jsonify({"msg": "bad request json"}), 400


@server.route("/admin/product", methods=['DELETE'])
def admin_product_delete():
    product_id = request.args.get("product_id", None)
    if product_id:
        ProductRepositoryRelationDB.delete_product(product_id)
        return "succ", 200
    else:
        return jsonify({"msg": "bad request"}), 400


if __name__ == "__main__":
    db.create_all()
    changeMessageConsumer = ChangeMessageConsumer(CUDMessageHandler())
    changeMessageConsumer.start_consuming_thread()
    server.run(host='0.0.0.0', port=5000)
