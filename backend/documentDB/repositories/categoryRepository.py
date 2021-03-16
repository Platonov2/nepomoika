from backend.documentDB.connector import categories_collection


def category_save(insert_data) -> None:
    categories_collection.insert_one(insert_data)


def category_update(update_criteria, update_data) -> None:
    categories_collection.update(update_criteria, update_data)


def category_remove(remove_criteria) -> None:
    categories_collection.remove(remove_criteria)


def category_get(search_criteria) -> {}:
    return categories_collection.find(search_criteria)
