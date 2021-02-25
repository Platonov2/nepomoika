import datetime

from flask_sqlalchemy import SQLAlchemy
from server import server
from sqlalchemy.dialects.postgresql import VARCHAR, TEXT

db = SQLAlchemy(server)
# migrate = Migrate(server, db)

# -------------------model tables-------------------------


class Category(db.Model):
    __tablename__ = 'product_category'
    id = db.Column(db.Integer, primary_key=True)

    parent_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    category_name = db.Column(db.String(255), nullable=False)

    children_categories = db.relationship('Category', cascade="all,delete", backref=db.backref('parent_category', remote_side=[id]))

    def serialize(self):
        children_list = [e.id for e in self.children_categories]
        return {
            'id': self.id,
            'category_name': self.category_name,
            'parent_category_id': self.parent_id,
            'children_categories_id': children_list
        }


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    image_link = db.Column(db.String(255), nullable=False)
    product_category_id = db.Column(db.Integer, db.ForeignKey("product_category.id"))

    product_category = db.relationship('Category', backref=db.backref('products', lazy=True))

    def serialize(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'product_price': self.product_price,
            'image_link': self.image_link,
            'product_category_id': self.product_category_id,
        }
