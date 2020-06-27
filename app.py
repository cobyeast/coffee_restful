import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
from flask_marshmallow import Marshmallow

from main.routes import Item, ItemList
from security import authenticate, idenity

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRESQL_URI')

db = SQLAlchemy(app)
mm = Marshmallow(app)

# @desc       Auth Endpoint 
# @route      /auth
jwt = JWT(app, authenticate, idenity)

app.add_url_rule('/api/<string:name>', view_func=Item.as_view('item'))
app.add_url_rule('/api', view_func=ItemList.as_view('itemlist'))


if __name__ == '__main__':
  app.run(port=os.getenv('PORT', default=8000), debug=True)