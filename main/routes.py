from pprint import pprint
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt import jwt_required

from models.items import Item as ItemModel, item_schema, items_schema
from config import db

items = []

class Item(MethodView):
  """
  @Item class: acts, as the introductory route with 'GET' and 'POST' requests.
  """
  @staticmethod
  def filters_by(items, name):
    for x in items:
      if x['name'] == name: yield x

  # @jwt_required()
  def get(self, name):
    one_item = ItemModel.query.filter_by(name=name).first()
    return item_schema.jsonify(one_item), 200

    # item = next(self.filter_by(items, name), None)
    # return {'item': item}, 200 if item else 404
  
  def post(self, name):
    # data = request.get_json(silent=True)
    # req_item = dict(name=name, price=data['price'], description=data['description'])
    # print(req_item)

    # res = item_schema.dump(req_item)
    # pprint(res, indent=2)

    # if not request.json or not 'name' in request.json:
    #   return 400

    price = request.json['price']
    description = request.json['description']

    new_item = ItemModel(name, price, description)

    db.session.add(new_item)
    db.session.commit()

    return item_schema.jsonify(new_item), 201

    # jsonify({'name': req_item.name, 'price': req_item.price, 'description': req_item.description}), 201
    
    # if next(self.filter_by(items, name), None):
    #   return {'message': f'An item with name "{name}" already exists'}
    # data = request.get_json(silent=True)
    # item = {'name': name, 'price': data['price'],'description': data['description']}
    # item, 201 if item else 404
  
  def delete(self, name):
    global items
    for x in items:
      if x['name']:
        items = list((x for x in items if x['name'] != name))
        return {'message': f'item: {name}, was deleted'}, 202
    return {'message': 'item was not found'}, 404
  
  def put(self, name):
    data = request.get_json()
    item = next(self.filters_by(items, name), None)
    if item is None:
      item = {'name': name, 'price': data['price'],'description': data['description']}
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
    all_items = ItemModel.query.all()
    res = items_schema.dump(all_items)
    return jsonify(res)