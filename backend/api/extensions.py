from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
