import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRESQL_URI')


@app.before_first_request
def create_tables():
    db.create_all()


def load_routes():
  from main.routes import Item, ItemList

  app.add_url_rule('/api/<string:name>', view_func=Item.as_view('item'))
  app.add_url_rule('/api', view_func=ItemList.as_view('itemlist'))


if __name__ == '__main__':
  from config import db
  from models.users import User
  from models.items import Item

  load_routes()

  db.init_app(app)
  app.run(port=os.getenv('PORT', default=8000), debug=True)

  # db.create_all()