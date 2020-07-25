"""
@desc: CRUD items routes for app.py module, with an additional route for 'GET' all requests.

Author: C. Eastwood (07/24/2020)
"""


from pprint import pprint
from flask import request, jsonify, session
from flask.views import MethodView

from models.items import ItemModel, item_schema, items_schema
from config import db


class Item(MethodView):
  """
  @desc: handles 'GET', 'POST' requests with name as url parameter.
  @route: /api/items/<name>
  """

  def get(self, name):

    items = ItemModel.query.filter_by(name=name).all()

    if not items:
      return 204

    else:
      return items_schema.jsonify(items), 200

  def post(self, name):

    req = request.get_json(silent=True)

    # Destructure from request object
    name, price, desc = (req[i] for i in req)

    if not req:
      return 204

    else:
      item = ItemModel(name, price, description)

      db.session.add(item)
      db.session.commit()

      return item_schema.jsonify(item), 201

class ItemEdit(MethodView):
  """
  @desc: handles 'PUT', 'DELETE' requests with id as url parameter.
  @route: /api/items/<id>
  """

  def put(self, _id):

    # Verify current user is authorized on this route
    if not session.get('check'):
      return 401

    else:
      req = request.get_json(silent=True)

      name, price, desc = (req[i] for i in req)
      item = ItemModel.query.get(_id)

    # Creates new item if none exists
    if not item:
      new_item = ItemModel(name, price, description)
      db.session.add(new_item)

    else:
      # Create item dict
      item.name = name
      item.price = price
      item.description = description

    # Commit changes to postgres
    db.session.commit()

    return {'msg': f'Item {item.name} was successfully updated.'}, 201
  
  def delete(self, _id):

    if not session.get('check'):
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
  
  def get(self):

    items = ItemModel.query.all()

    if not items:
      return 204

    res = items_schema.dump(items)
    return jsonify(res)