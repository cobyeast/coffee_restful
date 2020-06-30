from datetime import datetime
from config import db, ma, bcrypt

class UserModel(db.Model):
  __tablename__= 'user'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(25))
  password = db.Column(db.String(100))
  created = db.Column(db.DateTime, default=datetime.now)

  def __init__(self, username, password):
    self.username = username
    self.password = password
  
  @staticmethod
  def set_hash(password):
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    return pw_hash

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  # def check_hash(cls, username, password):
  #   user = cls.query.filter_by(username).first()
  #   pw_hash = user.password
  #   return bcrypt.check_password_hash(pw_hash, password)

  def __repr__(self):
    return f'{self.__class__.__name__}'

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
      model = UserModel
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