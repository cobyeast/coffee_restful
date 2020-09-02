"""
@desc: item models with additional serialization, and query support for items.py routes.
@made: (07/23/2020), by Coby Eastwood

"""

from config import db, ma
from marshmallow_sqlalchemy import ModelSchema


class ItemModel(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    price = db.Column(db.Float(precision=2))
    description = db.Column(db.String(150))

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        return f'{self.__class__.__name__}'


class ItemSchema(ModelSchema):
    class Meta:
        model = ItemModel


# Set schemas for query searches
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)