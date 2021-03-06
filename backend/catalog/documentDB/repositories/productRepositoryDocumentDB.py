from backend.catalog.documentDB.connector import products_collection


class ProductRepositoryDocumentDB:

    @staticmethod
    def product_create(insert_product) -> None:
        products_collection.insert_one(insert_product)

    @staticmethod
    def product_update(update_product) -> None:
        products_collection.update({"product_id": update_product["product_id"]}, update_product)

    @staticmethod
    def product_delete(product_id) -> None:
        products_collection.remove({"product_id": product_id})

    @staticmethod
    def get_product_by_id(product_id) -> {}:
        return products_collection.find_one({"product_id": product_id}, {"_id": 0})

    @staticmethod
    def get_products_by_category_id(category_id) -> []:
        results = products_collection.find({"product_category_id": category_id}, {"_id": 0})
        return [r for r in results]
