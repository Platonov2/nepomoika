from enum import Enum


class MessageCollection(Enum):
    PRODUCT = 1
    CATEGORY = 2

    def serialize(self):
        return 'collection'