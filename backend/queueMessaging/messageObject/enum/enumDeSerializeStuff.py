from backend.queueMessaging.messageObject.enum.messageType import MessageType
from backend.queueMessaging.messageObject.enum.messageCollection import MessageCollection

PUBLIC_ENUMS = {
    'MessageType': MessageType,
    'MessageCollection': MessageCollection
}

def from_string_to_enum(string: str):
    name, member = string.split(".")
    return getattr(PUBLIC_ENUMS[name], member)