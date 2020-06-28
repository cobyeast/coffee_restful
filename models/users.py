from datetime import datetime

from config import *

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(25))
  password = db.Column(db.String(25))
  created = db.Column(db.DateTime, default=datetime.now)

  def __init__(self, username, password):
    self.username = username
    self.password = password
  
  def __repr__(self):
    return f'{self.__class__.__name__}'

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
      model = User
      load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# class User:
#   def __init__(self, _id, username, password):
#     self._id = _id
#     self.username = username
#     self.password = password

# class UserSchema(Schema):
#   username = fields.String()
#   password = fields.String()

#   @post_load
#   def create_users(self, data, **kwargs):
#     return User(**data)


# schema = UserSchema()
# user = schema.load()

# result = schema.dumps(user)