from flask import request, jsonify
from flask.views import MethodView
from flask_jwt import jwt_required

items = []

class Item(MethodView):
  """
  @Item class: acts, as the introductory route with 'GET' and 'POST' requests.
  """
  @staticmethod
  def filter_by(items, name):
    for x in items:
      if x['name'] == name: yield x

  # @jwt_required()
  def get(self, name):
    item = next(self.filter_by(items, name), None)
    return {'item': item}, 200 if item else 404
  
  def post(self, name):
    if next(self.filter_by(items, name), None):
      return {'message': f'An item with name "{name}" already exists'}

    data = request.get_json(silent=True)
    item = {'name': name, 'price': data['price']}
    items.append(item)
    return item, 201 if item else 404
  
  def delete(self, name):
    global items
    for x in items:
      if x['name']:
        items = list((x for x in items if x['name'] != name))
        return {'message': f'item: {name}, was deleted'}, 202
    return {'message': 'item was not found'}, 404
  
  def put(self, name):
    data = request.get_json()
    item = next(self.filter_by(items, name), None)
    if item is None:
      item = {'name': name, 'price': data['price']}
      items.append(item)
    else:
      item.update(data)
    return item

class ItemList(MethodView):
  """
  @ItemList class: acts, as the introductory route with a 'GET' requests.
  """
  # @jwt_required()
  def get(self):
    return {'items': items}