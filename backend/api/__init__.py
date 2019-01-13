from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS
from flask_migrate import Migrate

from api.blueprints import contact

"""Create the instances of the Flask extensions in the global scope"""

mail = Mail()
migrate = Migrate()
db = SQLAlchemy()


"""Application factory function"""

def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.DevelopmentConfig')

    initialize_extensions(app)
    register_blueprints(app)
    CORS(app)

    return app


"""Helper functions"""

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db, directory='api/migrations')


"""Registering blueprints"""

def register_blueprints(app):
    app.register_blueprint(contact.contact)
