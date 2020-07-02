from flask import request, jsonify, session
from flask.views import MethodView
from werkzeug.wrappers import Response
# from flask_jwt import jwt_required

from models.users import UserModel, user_schema, users_schema
from config import db, bcrypt


# @jwt_required is an optional decorator added for additional security
class User(MethodView):
  """
  @desc: handles 'GET', 'POST', 'DELETE', and 'PUT' requests with an id as url parameter.
  @route: /api/users/<id>
  """

  # @jwt_required()
  def get(self, _id):

    current_user = session.get('username')

    if not current_user:
      return 400
    
    user = UserModel.query.filter_by(id=_id).first()

    # Check if requested user is the same as user loggedin
    if current_user == user.username:
      return user_schema.jsonify(user), 200
    else:
      return {'msg': 'Not authorized to access this route.'}, 401
  
  def put(self, _id):

    data = request.get_json(silent=True)
    user = UserModel.query.get(_id)

    if not user:
      return 400

    user.username = data['username']
    db.session.commit()

    return {'msg': f'User {user.username} was successfully updated.'}, 201
  
  # @jwt_required()
  def delete(self, _id):

    current_user = session.get('username')

    if not current_user:
      return 400

    user = UserModel.query.get(_id)

    if user.username == current_user:
      db.session.delete(user)
      db.session.commit()

    return {'msg': f'User {user.username} was successfully deleted.'}, 202

class UserList(MethodView):
  """
  @desc: handles 'GET' all requests with url no parameters.
  @route: /api/users
  """

  # @jwt_required()
  def get(self):

    check = session.get('check')

    if not check:
      return 400

    users = UserModel.query.all()

    if check == True and users:
      user = ( {'id': user.id, 'username': user.username} for user in users )
      res = users_schema.dump(user)
      return jsonify(res), 200
    else:
      return {'msg': 'Not authorized to access this route.'}, 401