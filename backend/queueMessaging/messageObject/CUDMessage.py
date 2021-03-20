from backend.queueMessaging.messageObject.enum.messageType import MessageType
from backend.queueMessaging.messageObject.enum.messageCollection import MessageCollection


class CUDMessage:
    def __init__(self, message_type: MessageType, message_collection: MessageCollection, message_body: {}):
        self.message_type = message_type
        self.message_collection = message_collection
        self.message_body = message_body

    def serialize(self):
        return {
            'message_type': self.message_type.serialize(),
            'message_collection': self.message_collection.serialize(),
            'message_body': self.message_body,
        }