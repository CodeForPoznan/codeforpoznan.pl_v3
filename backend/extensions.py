from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

"""Create the instances of the Flask extensions in the global scope"""

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
