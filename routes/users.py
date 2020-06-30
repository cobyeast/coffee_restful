from pprint import pprint
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt import jwt_required

from models.users import UserModel, user_schema, users_schema
from config import db, bcrypt
from routes.utils import check_hash

class User(MethodView):
  """
  @desc: handles 'GET', 'POST', 'DELETE', and 'PUT' requests with an id as parameter.
  @route: /api/users/<id>
  """

  # @jwt_required()
  def get(self, _id):

    user = UserModel.query.filter_by(id=_id).first()

    if not user:
      return 400

    return user_schema.jsonify(user), 200
  
  def put(self, _id):

    data = request.get_json(silent=True)
    user = UserModel.query.get(_id)

    if not user:
      return 400

    user.username = data['username']
    db.session.commit()

    return {'msg': f'User {user.username} was successfully updated.'}, 201
  
  def delete(self, _id):

    data = request.get_json(silent=True)

    username = data['username']
    password = data['password']

    user = UserModel.query.get(_id)

    if not user:
      return 400

    check = check_hash(username, password)

    if check[0] == True:
      db.session.delete(user)
      db.session.commit()

    return {'msg': f'User {user.username} was successfully deleted.'}, 202 if check[0] else 401

class UserRegister(MethodView):
  """
  @desc: handles 'POST' requests with no parameters.
  @route: /api/users/register
  """

  def post(self):

    data = request.get_json(silent=True)

    username = data['username']
    password = data['password']

    if UserModel.find_by_username(username):
      return {'msg': f'User {username} already exists.'}, 400

    pw_hash = UserModel.set_hash(password)
    user = UserModel(username, pw_hash)

    db.session.add(user)
    db.session.commit()

    return {'msg': f'User {user.username} was successfully created.'}, 201

class UserList(MethodView):
  """
  @desc: handles 'GET' all requests with no parameters.
  @route: /api/users
  """
  # @jwt_required()
  def get(self):

    data = request.get_json(silent=True)

    username = data['username']
    password = data['password']

    if not username:
      return 400

    check = check_hash(username, password)
    users = UserModel.query.all()

    if check[0] == True:
      res = users_schema.dump(users)
      return jsonify(res), 200
    else:
      return {'msg': 'Not authorized to access this route.'}, 401