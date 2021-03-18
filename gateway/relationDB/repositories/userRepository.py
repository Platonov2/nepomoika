from relationDB.models import db, User, UserRole
from hashlib import sha256


def create_new_user(username: str, password: str, role: str) -> None:
    new_user = User(username=username,
                    password=sha256(password.encode('utf-8')).hexdigest())
    db.session.add(new_user)
    db.session.flush()
    new_role = UserRole(user_id=new_user.id, role_name=role)
    db.session.add(new_role)
    db.session.commit()


def get_user_by_login(username: str) -> User:
    return db.session.query(User).filter_by(username=username).one()


def get_user_role(username: str) -> UserRole:
    user = get_user_by_login(username)
    return db.session.query(UserRole).filter_by(user_id=user.id).one()
