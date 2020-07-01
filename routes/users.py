from flask import request, jsonify, session
from flask.views import MethodView
from flask_jwt import jwt_required
from werkzeug.wrappers import Response

from models.users import UserModel, user_schema, users_schema
from config import db, bcrypt

class User(MethodView):
  """
  @desc: handles 'GET', 'POST', 'DELETE', and 'PUT' requests with an id as url parameter.
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

    user = UserModel.query.get(_id)

    if not user:
      return 400

    check = session.get('check')

    if check == True:
      db.session.delete(user)
      db.session.commit()

    return {'msg': f'User {user.username} was successfully deleted.'}, 202

class UserList(MethodView):
  """
  @desc: handles 'GET' all requests with url no parameters.
  @route: /api/users
  """
  @jwt_required()
  def get(self):

    username = session.get('username')

    if not username:
      return 400

    check = session.get('check')
    users = UserModel.query.all()

    if check == True:
      res = users_schema.dump(users)
      return jsonify(res), 200
    else:
      return {'msg': 'Not authorized to access this route.'}, 401