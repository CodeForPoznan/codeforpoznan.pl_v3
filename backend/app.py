from flask import Flask

from backend.blueprints.contact import contact
from backend.extensions import db, mail, migrate


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object('backend.config.DevelopmentConfig')

    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app):
    """Helper functions"""
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db, directory='migrations')


def register_blueprints(app):
    """Registering blueprints"""
    app.register_blueprint(contact)
