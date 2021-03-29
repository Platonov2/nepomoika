from queueMessaging.messageHandlers.iMessageHandler import IMessageHandler
from relationDB.repositories.orderRepository import OrderRepository
from relationDB.models.order import Order


class OrderHandler(IMessageHandler):

    def handle(self, order_message: {}):
        new_order = Order(order_message["sum"], order_message["product_list"])
        OrderRepository.create_new_order(order_message["user_id"], new_order)

