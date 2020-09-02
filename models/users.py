"""
@desc: user models with additional serialization, and query support for users.py routes.
@made: (07/23/2020), by Coby Eastwood

"""

from datetime import datetime
from config import db, ma, bcrypt

from marshmallow_sqlalchemy import ModelSchema


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    password = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Hashes password upon registration
    def set_hash(self, password):
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        return pw_hash

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def __repr__(self):
        return f'{self.__class__.__name__}'


class UserSchema(ModelSchema):
    class Meta:
        model = UserModel


# Set schemas for query searches
user_schema = UserSchema()
users_schema = UserSchema(many=True)