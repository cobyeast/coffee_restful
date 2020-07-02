import os
import requests

from flask import request, jsonify, session
from flask.views import MethodView
from dotenv import load_dotenv

from app import app
from config import db, bcrypt
from models.users import UserModel
from routes.utils import check_hash

load_dotenv()

PORT = os.getenv('PORT')


class Register(MethodView):
  """
  @desc: handles 'POST' requests with url no parameters.
  @route: /api/users/register
  """

  def post(self):

    data = request.get_json(silent=True)

    username = data['username']
    password = data['password']

    # Check if username has already been registered
    if UserModel.find_by_username(username):
      return {'msg': f'User {username} already exists.'}, 400

    pw_hash = UserModel.set_hash(password)
    user = UserModel(username, pw_hash)

    db.session.add(user)
    db.session.commit()

    return {'msg': f'User {user.username} was successfully created.'}, 201

class Login(MethodView):
  """
  @desc: handles 'POST' requests with url no parameters.
  @route: /api/users/login
  """
  
  def post(self):

    data = request.get_json(silent=True)

    username = data['username']
    password = data['password']

    # Checks typed password matches hashed password
    check = check_hash(username, password)

    # Sends request to path /auth for JWT
    if check[0] == True:

      URL = f'http://localhost:{PORT}/auth'

      HEADERS = {
        'Content-Type': "application/json"
      }

      PARAMS = {
        'username': username, 
        'password': password
      }

      res = requests.post(url=URL, json=PARAMS, headers=HEADERS).json()

      # Sets session variables
      session['username'] = username
      session['jwt'] = res['access_token']
      session['check'] = True

      return {'msg': f'Successfully login for {username}'}, 200