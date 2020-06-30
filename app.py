import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt import JWT

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRESQL_URI')


@app.before_first_request
def create_tables():
  with app.app_context():
    db.create_all()


# Avoid circual imports
def load_routes():
  from security import authenticate, idenity
  from routes.items import Item, ItemEdit, ItemList
  from routes.users import User, UserList, UserRegister

  jwt = JWT(app, authenticate, idenity)

  app.add_url_rule('/api/items/<string:name>', view_func=Item.as_view('item'))
  app.add_url_rule('/api/items/<int:_id>', view_func=ItemEdit.as_view('ItemEdit'))
  app.add_url_rule('/api/items', view_func=ItemList.as_view('itemlist'))

  app.add_url_rule('/api/users/<int:_id>', view_func=User.as_view('user'))
  app.add_url_rule('/api/users/register', view_func=UserRegister.as_view('userregister'))
  app.add_url_rule('/api/users', view_func=UserList.as_view('userlist'))


if __name__ == '__main__':
  from config import db
  from models.users import UserModel
  from models.items import ItemModel

  load_routes()

  db.init_app(app)
  app.run(port=os.getenv('PORT', default=8000), debug=True)