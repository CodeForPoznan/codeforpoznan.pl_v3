from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

"""Create the instances of the Flask extensions in the global scope"""

migrate = Migrate()
db = SQLAlchemy()
jwt = JWTManager()
