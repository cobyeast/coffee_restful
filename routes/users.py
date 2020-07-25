"""
@desc: CRUD users routes for app.py module, with an additional route for 'GET' all requests.

Author: C. Eastwood (07/24/2020)
"""


from flask import request, jsonify, session
from flask.views import MethodView
from werkzeug.wrappers import Response

from models.users import UserModel, user_schema, users_schema
from config import db, bcrypt


class User(MethodView):
  """
  @desc: handles 'GET', 'POST', 'DELETE', and 'PUT' requests with an id as url parameter.
  @route: /api/users/<id>
  """

  def get(self, _id):
    
    user = UserModel.query.filter_by(id=_id).first()

    # Users can only access their own information
    if session.get('username') == user.username:
      return user_schema.jsonify(user), 200
      
    else:
      return {'msg': 'Not authorized to access this route.'}, 401
  
  def put(self, _id):

    req = request.get_json(silent=True)

    # Query users by id
    user = UserModel.query.get(_id)

    if not user:
      return 400

    else:
      user.username = req['username']
      db.session.commit()
      return {'msg': f'User {user.username} was successfully updated.'}, 201
  
  def delete(self, _id):

    user = UserModel.query.get(_id)

    # Users can only delete their accounts
    if user.username == session.get('username'):
      db.session.delete(user)
      db.session.commit()
      return {'msg': f'User {user.username} was successfully deleted.'}, 202
      
    else:
      return 400

class UserList(MethodView):
  """
  @desc: handles 'GET' all requests under the specified route, taking no url parameters.
  @route: /api/users
  """

  def get(self):

    users = UserModel.query.all()

    if session.get('check'):

      # Make a dict object containing all users
      user = ( {'id': user.id, 'username': user.username} for user in users )
      res = users_schema.dump(user)
      return jsonify(res), 200

    else:
      return 400