import os

from relationDB.models import db, User, UserRole
from hashlib import sha256
from sqlalchemy import exc

class UserRepository:

    @staticmethod
    def create_new_user(username: str, password: str, role: str) -> None:
        new_user = User(username=username,
                        password=sha256((password + os.environ["PASS_SALT"]).encode('utf-8')).hexdigest())
        db.session.add(new_user)
        db.session.flush()
        new_role = UserRole(user_id=new_user.id, role_name=role)
        db.session.add(new_role)
        db.session.commit()

    @staticmethod
    def compare_user_pass(username_from_form: str, password_from_form: str) -> bool:
        try:
            user = UserRepository.get_user_by_login(username_from_form)
            return user.password == sha256((password_from_form + os.environ["PASS_SALT"]).encode('utf-8')).hexdigest()
        except exc.SQLAlchemyError:
            return False


    @staticmethod
    def get_user_by_login(username: str) -> User:
        return db.session.query(User).filter_by(username=username).one()

    @staticmethod
    def get_user_role(username: str) -> UserRole:
        user = UserRepository.get_user_by_login(username)
        return db.session.query(UserRole).filter_by(user_id=user.id).one()
