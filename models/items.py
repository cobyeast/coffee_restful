from config import db, ma

class Item(db.Model):
  __tablename__= 'item'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(25))
  price = db.Column(db.Integer)
  description = db.Column(db.String(150))

  def __init__(self, name, price, description):
    self.name = name
    self.price = price
    self.description = description
  
  def __repr__(self):
    return f'{self.__class__.__name__}'

class ItemSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Item
    load_instance = True

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)