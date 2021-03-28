import requests

from server import server
from flask import request, jsonify
from documentDB.models.shoppingCart import ShoppingCart
from queueMessaging.consumers.changeMessageConsumer import ChangeMessageConsumer
from queueMessaging.messageHandlers.CUDMessageHandler import CUDMessageHandler
from documentDB.repositories.shoppingCartRepository import ShoppingCartRepository


@server.route("/cart/add", methods=['POST'])
def shopping_cart_add_product():
    user_id = request.headers.get('x-user-id', None)
    product_id = request.args.get("product_id", None)
    if user_id and product_id:
        product = get_product_from_admin(product_id)
        ShoppingCartRepository.add_new_product_in_card(user_id, product)
        return "succ", 200
    else:
        return jsonify({"msg": "Bad request"}), 400


@server.route("/cart/remove", methods=['POST'])
def shopping_cart_remove_product():
    user_id = request.headers.get('x-user-id', None)
    product_id = request.args.get("product_id", None)
    if user_id and product_id:
        ShoppingCartRepository.remove_product_in_card(user_id, product_id)
        return "succ", 200
    else:
        return jsonify({"msg": "Bad request"}), 400


@server.route("/cart/get", methods=['GET'])
def get_shopping_cart():
    user_id = request.headers.get('x-user-id', None)
    if user_id:
        shopping_cart = ShoppingCartRepository.get_product_card(user_id)
        return shopping_cart.serialize_with_list_of_products_and_total_price(), 200
    else:
        return jsonify({"msg": "Bad request"}), 400


def get_product_from_admin(product_id):
    headers = {'x-user-role': 'cart'}
    args = {'product_id': product_id}
    resp = requests.get('http://backend:5000/cart/product', params=args, headers=headers)
    return resp.json()


if __name__ == "__main__":
    changeMessageConsumer = ChangeMessageConsumer(CUDMessageHandler())
    changeMessageConsumer.start_consuming_thread()
    server.run(host='0.0.0.0', port=5000)
