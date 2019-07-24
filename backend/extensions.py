from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

"""Create the instances of the Flask extensions in the global scope"""

api = Api()
db = SQLAlchemy()
jwt = JWTManager()
mail = Mail()
migrate = Migrate()
