

def from_string_to_enum(string: str, enum_class):
    enum_value = string.split(".")[1]
    return getattr(enum_class, enum_value)