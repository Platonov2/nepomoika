from relationDB.models.enum.orderStatus import OrderStatus

PUBLIC_ENUMS = {
    'OrderStatus': OrderStatus
}


def from_string_to_enum(string: str):
    name, member = string.split(".")
    return getattr(PUBLIC_ENUMS[name], member)
