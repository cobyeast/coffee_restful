"""
@desc: function provides support for auth.py.
@made: (07/25/2020), by Coby Eastwood

"""

from config import bcrypt
from models.users import UserModel


def check_hash(username, password):

    # Small function for checking hashed passwords

    user = UserModel.query.filter_by(username=username).first()
    return (bcrypt.check_password_hash(user.password, password), user)
