import os
from dotenv import load_dotenv
from flask import jsonify

from app import app
from models.users import UserModel
from config import bcrypt, db
# from middleware.middleware import after_req

load_dotenv()


admins = [
  UserModel(os.getenv('ADMIN'), UserModel.set_hash(os.getenv('PASSWORD')))
]

# Set Admins by Default; set_admin = True
# set_admin = True

# @app.after_request
# def default_admin():
#   if set_admin == True:
#     admin = next(one for one in admins)
#     print(admin)
#     db.session.add(admin)
#     db.session.commit()

# @app.after_request(after_req)
def authenticate(username, password):
  user = UserModel.query.filter_by(username=username).first()
  if user and bcrypt.check_password_hash(user.password, password):
    return user

def idenity(payload):
  user_id = payload['identity']
  return UserModel.query.get(user_id)