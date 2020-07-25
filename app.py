"""
Simple Flask CRUD Api
v.1.0.1

@desc: main app module, setups config, and initializes api endpoints

Author: C. Eastwood (07/25/2020)
"""


import os
from dotenv import load_dotenv
from flask import Flask, session
from flask_jwt import JWT

# Optional middleware
# from middleware.middleware import Middleware

load_dotenv()


app = Flask(__name__)

# Optional middleware function to set JWT token in header for authentication
# app.wsgi_app = Middleware(app.wsgi_app)

app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRESQL_URI')

# Create tables before first api call
@app.before_first_request
def create_tables():
  with app.app_context():
    db.create_all()


# Avoid circual imports
def load_routes():
  from security import authenticate, idenity
  from routes.items import Item, ItemEdit, ItemList
  from routes.users import User, UserList
  from routes.auth import Login, Register

  jwt = JWT(app, authenticate, idenity) # set to path /auth by default

  # Lists all api endpoints, with <:> values set as params
  app.add_url_rule('/api/items/<string:name>', view_func=Item.as_view('item'))
  app.add_url_rule('/api/items/<int:_id>', view_func=ItemEdit.as_view('itemedit'))
  app.add_url_rule('/api/items', view_func=ItemList.as_view('itemlist'))

  app.add_url_rule('/api/users/<int:_id>', view_func=User.as_view('user'))
  app.add_url_rule('/api/users', view_func=UserList.as_view('userlist'))

  app.add_url_rule('/api/auth/login', view_func=Login.as_view('login'))
  app.add_url_rule('/api/auth/register', view_func=Register.as_view('register'))


@app.route('/api/auth/logout', methods=['GET', 'POST'])
def logout():
  session.clear()
  return {'msg': 'Successful logout'}, 200


if __name__ == '__main__':
  from config import db
  from models.users import UserModel
  from models.items import ItemModel

  load_routes()

  db.init_app(app)
  app.run(port=os.getenv('PORT', default=8000), debug=True)