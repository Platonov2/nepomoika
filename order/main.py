from server import server
from relationDB.models.relationModels import db
from queueMessaging.consumers.OrderConsumer import OrderConsumer
from queueMessaging.messageHandlers.orderHandler import OrderHandler
from relationDB.repositories.orderRepository import OrderRepository, OwnerException
from relationDB.models.enum.enumDeserialize import from_string_to_enum
from relationDB.models.enum.orderStatus import OrderStatus
from flask import request, jsonify
from functools import wraps


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        header = request.headers.get('x-user-role', None)
        if header:
            if request.headers.get('x-user-role') != "admin":
                return jsonify({"msg": "wrong permissions"}), 401
        else:
            return jsonify({"msg": "bad user role header"}), 400
        return f(*args, **kwargs)
    return decorated_function


@server.route('/order/getall', methods=["GET"])
# @admin_only
def get_all_orders():
    orders = OrderRepository.get_all_orders()
    return {"orders": orders}, 200


@server.route('/order/get', methods=["GET"])
def get_own_orders():
    user_id = request.headers.get('x-user-id', None)
    if user_id:
        orders = OrderRepository.get_orders_by_user(int(user_id))
        return {"orders": orders}, 200
    else:
        return jsonify({"msg": "Bad request, not have user_id"}), 400


@server.route("/order/status", methods=["POST"])
# @admin_only
def change_order_status():
    aggregate_id = request.json.get("aggregate_id", None)
    order_status = request.json.get("order_status", None)
    if order_status and aggregate_id:
        orders = OrderRepository.change_order_status(aggregate_id, from_string_to_enum(order_status))
        return {"msg": "succ"}, 200
    else:
        return jsonify({"msg": "Bad request args"}), 400


@server.route("/order/cancel", methods=["POST"])
def cancel_order():
    user_id = request.headers.get('x-user-id', None)
    if user_id:
        aggregate_id = request.json.get("aggregate_id", None)
        if aggregate_id:
            # try:
            OrderRepository.change_order_status(aggregate_id, OrderStatus.CANCELED)
            return {"msg": "succ"}, 200
            # except OwnerException as e:
            #     return {"msg": e.txt}, 400
        else:
            return jsonify({"msg": "Bad request args"}), 400
    else:
        return jsonify({"msg": "Bad request, not have user_id"}), 400


if __name__ == "__main__":
    db.create_all()
    consumer = OrderConsumer(OrderHandler())
    consumer.start_consuming_thread()
    server.run(host='0.0.0.0', port=5000)
