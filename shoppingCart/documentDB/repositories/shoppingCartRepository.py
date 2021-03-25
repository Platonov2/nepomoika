from documentDB.connector import shopping_cart_collection
from documentDB.models.shoppingCart import ShoppingCart


class ShoppingCartRepository:

    @staticmethod
    def add_new_shopping_cart(user_id) -> None:
        shopping_cart_collection.insert_one({"user_id": user_id, "product_dict": {}})

    @staticmethod
    def add_new_product_in_card(user_id, product) -> None:
        shopping_card = ShoppingCartRepository.get_product_card(user_id)
        if shopping_card is None:
            ShoppingCartRepository.add_new_shopping_cart(user_id)
            shopping_card = ShoppingCartRepository.get_product_card(user_id)
        shopping_card.product_dict[str(product["product_id"])] = product
        ShoppingCartRepository.shopping_cart_update(shopping_card.serialize_without_prise())

    @staticmethod
    def remove_product_in_card(user_id, product_id) -> None:
        shopping_card = ShoppingCartRepository.get_product_card(user_id)
        del shopping_card.product_dict[product_id]
        ShoppingCartRepository.shopping_cart_update(shopping_card.serialize_without_prise())

    @staticmethod
    def update_product_in_card(user_id, product) -> None:
        shopping_card = ShoppingCartRepository.get_product_card(user_id)
        shopping_card.product_dict[str(product["product_id"])] = product
        ShoppingCartRepository.shopping_cart_update(shopping_card.serialize_without_prise())

    @staticmethod
    def shopping_cart_update(update_shopping_cart) -> None:
        shopping_cart_collection.update({"user_id": update_shopping_cart["user_id"]}, update_shopping_cart)

    @staticmethod
    def remove_shopping_cart(remove_shopping_cart) -> None:
        shopping_cart_collection.remove({"user_id": remove_shopping_cart["user_id"]})

    @staticmethod
    def update_product_in_all_shopping_carts(product) ->None:
        shopping_carts = shopping_cart_collection.find({"product_dict." + str(product["product_id"]): {"$exists": True}}) #{'product_list': {"$elemMatch": {"product_id": product["product_id"]}}}
        for shopping_cart in shopping_carts:
            ShoppingCartRepository.update_product_in_card(shopping_cart["user_id"], product)

    @staticmethod
    def delete_product_in_all_shopping_carts(product) -> None:
        shopping_carts = shopping_cart_collection.find({"product_dict." + str(product["product_id"]): {"$exists": True}})
        for shopping_cart in shopping_carts:
            ShoppingCartRepository.remove_product_in_card(shopping_cart["user_id"], str(product["product_id"]))

    @staticmethod
    def get_product_card(user_id) -> ShoppingCart:
        cart_form_mongo = shopping_cart_collection.find_one({"user_id": user_id}, {"_id": 0})
        return ShoppingCart(cart_form_mongo["user_id"], cart_form_mongo["product_dict"])

    # db.ShoppingCart.find( {product_list.2: {$exists: 1}})
    # db.ShoppingCart.find_one( {"user_id": 2})
    # mongo --host localhost --port 27017 -u root -p root