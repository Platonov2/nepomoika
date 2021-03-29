from relationDB.models.enum.orderStatus import OrderStatus


class Order:

    def __init__(self, order_sum: int, order_products: [], order_status=None):
        self.order_sum = order_sum
        self.order_products = order_products
        if order_status:
            self.order_status = order_status
        else:
            self.order_status = OrderStatus.UNCHECKED

    def change_status(self, new_status: OrderStatus) -> bool:
        if new_status == OrderStatus.CHECKED and self.order_status == OrderStatus.UNCHECKED:
            self.order_status = new_status
            return True
        if new_status == OrderStatus.COMPLETED and self.order_status == OrderStatus.CHECKED:
            self.order_status = new_status
            return True
        if new_status == OrderStatus.CANCELED and self.order_status == OrderStatus.UNCHECKED:
            self.order_status = new_status
            return True
        if new_status == OrderStatus.ABORTED:
            self.order_status = new_status
            return True
        return False

    def serialize(self):
        return {
            'order_sum': self.order_sum,
            'order_status': self.order_status.serialize(),
            'order_products': self.order_products
        }

    def serialize_status(self):
        return {
            'order_status': self.order_status.serialize(),
        }