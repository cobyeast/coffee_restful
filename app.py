import os
from dotenv import load_dotenv
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow

from main.routes import Item, ItemList

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRESQL_URI')


# @app.before_first_request
# def create_tables():
#     db.create_all()


# db = SQLAlchemy(app)
# mm = Marshmallow(app)

app.add_url_rule('/api/<string:name>', view_func=Item.as_view('item'))
app.add_url_rule('/api', view_func=ItemList.as_view('itemlist'))


if __name__ == '__main__':
  from models.users import User
  from models.items import Item
  from config import db

  app.run(port=os.getenv('PORT', default=8000), debug=True)
  db.create_all()