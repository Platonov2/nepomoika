from backend.catalog.documentDB.connector import categories_collection


class CategoryRepositoryDocumentDB:

    @staticmethod
    def category_create(insert_category) -> None:
        if insert_category["root_category_id"] is not None:
            root_category = CategoryRepositoryDocumentDB.get_category_by_id(insert_category["root_category_id"])
            root_category["children_categories_id"].append(insert_category["category_id"])  # TODO странные null при сохранении списка
            CategoryRepositoryDocumentDB.category_update(root_category)
        categories_collection.insert_one(insert_category)

    @staticmethod
    def category_update(update_category) -> None:
        categories_collection.update({"category_id": update_category["category_id"]}, update_category)

    @staticmethod
    def category_delete(remove_category) -> None:
        if remove_category["root_category_id"] is not None:
            root_category = CategoryRepositoryDocumentDB.get_category_by_id(remove_category["root_category_id"])
            root_category["children_categories_id"].remove(remove_category["category_id"])
            CategoryRepositoryDocumentDB.category_update(root_category)
        categories_collection.remove({"category_id": remove_category["category_id"]})

    @staticmethod
    def get_category_by_id(category_id) -> {}:
        return categories_collection.find_one({"category_id": category_id}, {"_id": 0})

    @staticmethod
    def get_all_root_category() -> []:
        results = categories_collection.find({"root_category_id": None}, {"_id": 0})
        return [r for r in results]

    @staticmethod
    def get_all_children_category(category_id) -> []:
        results = categories_collection.find({"root_category_id": category_id}, {"_id": 0})
        return [r for r in results]
