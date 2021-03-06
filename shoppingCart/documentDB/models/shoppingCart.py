class ShoppingCart:
    def __init__(self, user_id: int, product_dict: {}):
        self.user_id = user_id
        self.product_dict = product_dict
        self.sum = 0
        self.calculate_cart_sum()

    def calculate_cart_sum(self):
        self.sum = 0
        for key in self.product_dict.keys():
            self.sum += self.product_dict[key]["product_price"]

    def serialize_with_list_of_products_and_total_price(self):
        products = []
        for item in self.product_dict.items():
            products.append(item[1])
        return {
            'user_id': self.user_id,
            'product_list': products,
            'sum': self.sum,
        }

    def serialize_without_prise(self):
        return {
            'user_id': self.user_id,
            'product_dict': self.product_dict,
        }