import pymongo

connection = pymongo.Connection('mongo', 27017)

db = connection['ProductCatalog']

products_collection = db['products']
categories_collection = db['categories']