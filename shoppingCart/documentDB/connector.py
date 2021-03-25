from pymongo import MongoClient

client = MongoClient('mongo', 27017, username='root', password='root')

db = client['ShoppingCarts']

shopping_cart_collection = db['ShoppingCart']