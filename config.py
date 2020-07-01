from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt


from app import app

db = SQLAlchemy()
ma = Marshmallow(app)

bcrypt = Bcrypt(app)