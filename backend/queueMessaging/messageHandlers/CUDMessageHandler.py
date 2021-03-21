from backend.queueMessaging.messageObject.CUDMessage import CUDMessage
from backend.queueMessaging.messageObject.enum.messageType import MessageType
from backend.queueMessaging.messageObject.enum.messageCollection import MessageCollection
from backend.documentDB.repositories.productRepositoryDocumentDB import ProductRepositoryDocumentDB
from backend.documentDB.repositories.categoryRepositoryDocumentDB import CategoryRepositoryDocumentDB
from backend.queueMessaging.messageObject.enum.enumDeSerializeStuff import from_string_to_enum
from backend.queueMessaging.messageHandlers.iMessageHandler import IMessageHandler


class CUDMessageHandler(IMessageHandler):

    def handle_product_cud(self, message: CUDMessage):
        if message.message_type == MessageType.CREATE:
            ProductRepositoryDocumentDB.product_create(message.message_body)
        if message.message_type == MessageType.UPDATE:
            ProductRepositoryDocumentDB.product_update({"product_id": message.message_body["product_id"]}, message.message_body)
        if message.message_type == MessageType.DELETE:
            ProductRepositoryDocumentDB.product_delete(message.message_body) # {"product_id": message.message_body["product_id"]}

    def handle_category_cud(self, message: CUDMessage):
        if message.message_type == MessageType.CREATE:
            CategoryRepositoryDocumentDB.category_create(message.message_body)
        if message.message_type == MessageType.UPDATE:
            CategoryRepositoryDocumentDB.category_update({"category_id": message.message_body["category_id"]}, message.message_body)
        if message.message_type == MessageType.DELETE:
            CategoryRepositoryDocumentDB.category_delete(message.message_body) # {"category_id": message.message_body["category_id"]}

    def handle(self, cud_message_dict: {}):
        cud_message = CUDMessage(from_string_to_enum(cud_message_dict["message_type"]), #MessageType
                                 from_string_to_enum(cud_message_dict["message_collection"]), #MessageCollection
                                 cud_message_dict["message_body"])
        if cud_message.message_collection == MessageCollection.PRODUCT:
            self.handle_product_cud(cud_message)
        if cud_message.message_collection == MessageCollection.CATEGORY:
            self.handle_category_cud(cud_message)
