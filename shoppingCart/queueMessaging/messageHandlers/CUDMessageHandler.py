from queueMessaging.messageObject.CUDMessage import CUDMessage
from queueMessaging.messageObject.enum.messageType import MessageType
from queueMessaging.messageObject.enum.messageCollection import MessageCollection
from documentDB.repositories.shoppingCartRepository import ShoppingCartRepository
from queueMessaging.messageObject.enum.enumDeSerializeStuff import from_string_to_enum
from queueMessaging.messageHandlers.iMessageHandler import IMessageHandler


class CUDMessageHandler(IMessageHandler):

    def handle_product_cud(self, message: CUDMessage):
        if message.message_type == MessageType.UPDATE:
            ShoppingCartRepository.update_product_in_all_shopping_carts(message.message_body)
        if message.message_type == MessageType.DELETE:
            ShoppingCartRepository.delete_product_in_all_shopping_carts(message.message_body)

    def handle(self, cud_message_dict: {}):
        cud_message = CUDMessage(from_string_to_enum(cud_message_dict["message_type"]),
                                 from_string_to_enum(cud_message_dict["message_collection"]),
                                 cud_message_dict["message_body"])

        if cud_message.message_type == MessageType.UPDATE:
            ShoppingCartRepository.update_product_in_all_shopping_carts(cud_message.message_body)
        if cud_message.message_type == MessageType.DELETE:
            ShoppingCartRepository.delete_product_in_all_shopping_carts(cud_message.message_body)
