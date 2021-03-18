from backend.queueMessaging.MessageObject.messageType import MessageType
from backend.queueMessaging.MessageObject.messageCollection import MessageCollection


class CUDMessage:
    def __init__(self, message_type: MessageType, message_collection: MessageCollection, message_body: {}):
        self.message_type = message_type
        self.message_collection = message_collection
        self.message_body = message_body

    def serialize(self):
        return {
            'message_type': self.message_type,
            'message_collection': self.message_collection,
            'message_body': self.message_body,
        }