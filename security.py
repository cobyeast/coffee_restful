from flask import jsonify

from app import app
from config import bcrypt, db
from models.users import UserModel


def authenticate(username, password):
  user = UserModel.query.filter_by(username=username).first()
  if user and bcrypt.check_password_hash(user.password, password):
    return user

def idenity(payload):
  user_id = payload['identity']
  return UserModel.query.get(user_id)