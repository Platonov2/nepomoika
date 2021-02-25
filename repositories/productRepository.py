from models import db, Product


def create_new_product(product_name: str, product_price: int, image_link: str, product_category_id: int) -> None:
    new_product = Product(product_name=product_name,
                          product_price=product_price,
                          image_link=image_link,
                          product_category_id=product_category_id)
    db.session.add(new_product)
    db.session.commit()


def get_product_by_id(product_id: int) -> Product:
    return db.session.query(Product).filter_by(id=product_id).one()


def update_product(product_id: int, product_name: str, product_price: int, image_link: str, product_category_id: int) -> None:
    product = db.session.query(Product).filter_by(id=product_id).one()
    product.product_name = product_name
    product.product_price = product_price
    product.image_link = image_link
    product.product_category_id = product_category_id

    db.session.add(product)
    db.session.commit()


def delete_product(product_id: int) -> None:
    product = db.session.query(Product).filter_by(id=product_id).one()
    db.session.delete(product)
    db.session.commit()