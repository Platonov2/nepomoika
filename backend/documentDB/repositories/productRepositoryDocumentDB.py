from backend.documentDB.connector import products_collection


class ProductRepositoryDocumentDB:

    @staticmethod
    def product_create(insert_data) -> None:
        products_collection.insert_one(insert_data)

    @staticmethod
    def product_update(update_criteria, update_data) -> None:
        products_collection.update(update_criteria, update_data)

    @staticmethod
    def product_delete(remove_criteria) -> None:
        products_collection.remove(remove_criteria)

    @staticmethod
    def get_product_by_id(product_id) -> {}:
        return products_collection.find_one({"product_id": product_id}, {"_id": 0})

    @staticmethod
    def get_products_by_category_id(category_id) -> []:
        results = products_collection.find({"product_category_id": category_id}, {"_id": 0})
        return [r for r in results]
