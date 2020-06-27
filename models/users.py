from app import db, mm

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(25))
  password = db.Column(db.String(25))

class UserSchema(mm.ModelSchema):
    class Meta:
      model = User

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