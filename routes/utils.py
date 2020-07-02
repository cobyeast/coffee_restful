from config import bcrypt
from models.users import UserModel


# Checks typed password matches hashed password
def check_hash(username, password):
  user = UserModel.query.filter_by(username=username).first()
  return (
    bcrypt.check_password_hash(user.password, password),
    user
  )