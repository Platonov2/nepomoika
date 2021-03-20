from flask_sqlalchemy import SQLAlchemy
from backend.server import server
from sqlalchemy import event
from backend.queueMessaging.publishers.cahngeMessagePublisher import ChangeMessagePublisher
from backend.queueMessaging.messageObject.CUDMessage import CUDMessage
from backend.queueMessaging.messageObject.enum.messageType import MessageType
from backend.queueMessaging.messageObject.enum.messageCollection import MessageCollection


db = SQLAlchemy(server)
changeMessagePublisher = ChangeMessagePublisher()

# -------------------model tables-------------------------


class Category(db.Model):
    __tablename__ = 'product_category'
    id = db.Column(db.Integer, primary_key=True)

    parent_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    category_name = db.Column(db.String(255), nullable=False)

    children_categories = db.relationship('Category', cascade="all,delete", backref=db.backref('parent_category', remote_side=[id]))

    def serialize(self):
        children_list = [e.id for e in self.children_categories]
        # is_leaf = True
        # if len(children_list) > 0:
        #     is_leaf = False
        return {
            'category_id': self.id,
            'category_name': self.category_name,
            'root_category_id': self.parent_id,
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
            'product_id': self.id,
            'product_name': self.product_name,
            'product_price': self.product_price,
            'image_link': self.image_link,
            'product_category_id': self.product_category_id,
        }

# ------------------- table triggers-------------------------


@event.listens_for(Category, 'after_insert')
def category_insert(mapper, connection, target):
    changeMessagePublisher.publish_task(CUDMessage(MessageType.CREATE, MessageCollection.CATEGORY, target.serialize()).serialize())


@event.listens_for(Category, 'after_update')
def category_insert(mapper, connection, target):
    changeMessagePublisher.publish_task(CUDMessage(MessageType.UPDATE, MessageCollection.CATEGORY, target).serialize())


@event.listens_for(Category, 'after_delete')
def category_insert(mapper, connection, target):
    changeMessagePublisher.publish_task(CUDMessage(MessageType.DELETE, MessageCollection.CATEGORY, target).serialize())


@event.listens_for(Product, 'after_insert')
def product_insert(mapper, connection, target):
    changeMessagePublisher.publish_task(CUDMessage(MessageType.CREATE, MessageCollection.PRODUCT, target).serialize())


@event.listens_for(Product, 'after_update')
def product_insert(mapper, connection, target):
    changeMessagePublisher.publish_task(CUDMessage(MessageType.UPDATE, MessageCollection.PRODUCT, target).serialize())


@event.listens_for(Product, 'after_delete')
def product_insert(mapper, connection, target):
    changeMessagePublisher.publish_task(CUDMessage(MessageType.DELETE, MessageCollection.PRODUCT, target).serialize())