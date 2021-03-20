from flask_sqlalchemy import SQLAlchemy
from server import server


db = SQLAlchemy(server)

# -------------------model tables-------------------------


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'login': self.username,
            'password_hash': self.password,
        }


class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    role_name = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'role_name': self.role_name,
        }
