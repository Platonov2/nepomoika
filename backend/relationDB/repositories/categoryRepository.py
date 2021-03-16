from backend.relationDB.models import db, Category


def create_new_category(category_name: str, parent_category_id: int) -> None:
    parent_category = None
    if parent_category_id != -1:
        parent_category = db.session.query(Category).filter_by(id=parent_category_id).one()

    new_category = Category(category_name=category_name, parent_category=parent_category)
    db.session.add(new_category)
    db.session.commit()


def get_category_by_id(category_id: int) -> Category:
    return db.session.query(Category).filter_by(id=category_id).one()


def update_category(category_id: int, category_name: str, root_category_id: int) -> None:
    category = db.session.query(Category).filter_by(id=category_id).one()
    category.category_name = category_name

    if root_category_id is not None:
        parent_category = db.session.query(Category).filter_by(id=root_category_id).one()
        category.parent_category = parent_category

    db.session.add(category)
    db.session.commit()


def delete_category(category_id: int) -> None:
    category = db.session.query(Category).filter_by(id=category_id).one()
    db.session.delete(category)
    db.session.commit()


def get_all_root_category() -> [Category]:
    return db.session.query(Category).filter_by(parent_id=None).all()


def get_children_category(category_id: int) -> [Category]:
    root_category = db.session.query(Category).filter_by(id=category_id).one()
    return root_category.children_categories