from backend.queueMessaging.messageObject.CUDMessage import CUDMessage
from backend.queueMessaging.messageObject.enum.messageType import MessageType
from backend.queueMessaging.messageObject.enum.messageCollection import MessageCollection
from backend.documentDB.repositories.productRepository import product_delete, product_create, product_update


class MessageHandler:

    def handle_product_cud(self, message: CUDMessage):
        if message.message_type == MessageType.INSERT:
            product_create(message.message_body)
        if message.message_type == MessageType.UPDATE:
            product_update(message.message_body["product_id"], message.message_body)
        if message.message_type == MessageType.DELETE:
            product_delete(message.message_body)

    def cud_message_handle(self, message: {}):
        cud_message = CUDMessage()
        if message.message_collection == MessageCollection.PRODUCT:
            self.handle_product_cud(message)
