from enum import Enum


class OrderStatus(Enum):
    UNCHECKED = 0
    CHECKED = 1
    CANCELED = 2
    COMPLETED = 3
    ABORTED = 4

    def serialize(self):
        return str(self)