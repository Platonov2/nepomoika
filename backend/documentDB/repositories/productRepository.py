from backend.documentDB.connector import products_collection


def product_create(insert_data) -> None:
    products_collection.insert_one(insert_data)


def product_update(update_criteria, update_data) -> None:
    products_collection.update(update_criteria, update_data)


def product_delete(remove_criteria) -> None:
    products_collection.remove(remove_criteria)


def product_get(search_criteria) -> {}:
    return products_collection.find(search_criteria)
