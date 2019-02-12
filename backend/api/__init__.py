from flask import Flask
from flask_cors import CORS
from api.blueprints import contact, auth
from api.blueprints.auth import is_token_revoked
from api.extensions import mail, migrate, db, jwt


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
    jwt.init_app(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_revoked(decoded_token):
        return is_token_revoked(decoded_token)


"""Registering blueprints"""


def register_blueprints(app):
    app.register_blueprint(contact.contact)
    app.register_blueprint(auth.auth_blueprint)
