from config import db, ma

class ItemModel(db.Model):
  __tablename__= 'item'
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

class ItemSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = ItemModel
    load_instance = True

# Set schemas for query searches
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)