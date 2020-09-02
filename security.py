"""
@desc: uses created wrappers from config.py, and search query from user.py model to create serverside endpoint for registration, and login in the auth.py route.
@made: (07/23/2020), by Coby Eastwood

"""

from flask import jsonify

from app import app
from config import bcrypt, db
from models.users import UserModel


# Find user, then decrypt to ensure match
def authenticate(username, password):

    user = UserModel.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        return user


# Assigns payload at /auth endpoint
def idenity(payload):
    user_id = payload['identity']
    return UserModel.query.get(user_id)
