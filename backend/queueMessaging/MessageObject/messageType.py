from enum import Enum


class MessageType(Enum):
    CREATE = 1
    UPDATE = 2
    DELETE = 3

    def serialize(self):
        return 'type'