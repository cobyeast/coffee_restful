from pprint import pprint
from flask import request, jsonify, session
from flask.views import MethodView
# from flask_jwt import jwt_required

from models.items import ItemModel, item_schema, items_schema
from config import db


# @jwt_required is an optional decorator added for additional security
class Item(MethodView):
  """
  @desc: handles 'GET', 'POST' requests with name as url parameter.
  @route: /api/items/<name>
  """

  # @jwt_required()
  def get(self, name):

    items = ItemModel.query.filter_by(name=name).all()

    if not items:
      return 204

    return items_schema.jsonify(items), 200

  def post(self, name):

    data = request.get_json(silent=True)

    if not data and not data['price']:
      return 204

    item = ItemModel(name, data['price'], data['description'])

    db.session.add(item)
    db.session.commit()

    return item_schema.jsonify(item), 201

class ItemEdit(MethodView):
  """
  @desc: handles 'PUT', 'DELETE' requests with id as url parameter.
  @route: /api/items/<id>
  """

  def put(self, _id):

    check = session.get('check')

    # Check if user is loggedin
    if not check:
      return 401

    data = request.get_json(silent=True)
    
    name = data['name']
    price = data['price']
    description = data['description']

    item = ItemModel.query.get(_id)

    # Creates new item if none exists
    if not item:
      new_item = ItemModel(name, price, description)
      db.session.add(new_item)

    if item and name and price and description:
      item.name = name
      item.price = price
      item.description = description
    
    db.session.commit()

    return {'msg': f'Item {item.name} was successfully updated.'}, 201
  
  # @jwt_required()
  def delete(self, _id):

    check = session.get('check')

    if not check:
      return 401

    item = ItemModel.query.get(_id)

    if not item:
      return 204

    db.session.delete(item)
    db.session.commit()

    return {'msg': f'Item {item.name} was successfully deleted.'}, 202

class ItemList(MethodView):
  """
  @desc: handles 'GET' requests with no url parameters.
  @route: /api/items
  """
  
  # @jwt_required()
  def get(self):

    items = ItemModel.query.all()

    if not items:
      return 204

    res = items_schema.dump(items)
    return jsonify(res)