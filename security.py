import os
from dotenv import load_dotenv
from werkzeug.security import safe_str_cmp
from flask import jsonify

from models.users import User, UserSchema

load_dotenv()

users = [
  User(1, os.getenv('ADMIN'), os.getenv('PASSWORD'))
]

username_map = {user.username: user for user in users}
userid_map = {user.id: user for user in users}

def autheticate(username, password):
  users = User.query.all()
  user_schema = UserSchema(many=True)
  res = user_schema.dumps(users).data

  user = username_map.get(username, None)
  if user and safe_str_cmp(user.password, password):
    return jsonify({'user': res})

def idenity(payload):
  user_id = payload['identity']
  return userid_map.get(user_id, None)