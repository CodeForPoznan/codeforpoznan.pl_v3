from flask import Flask
from flask_cors import CORS

from backend.commands.populate_database import populate_database
from backend.extensions import db, mail, migrate, jwt
from backend.blueprints import auth
from backend.blueprints.contact import contact
from backend.blueprints.participants import participants


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object('backend.config.DevelopmentConfig')
    app.cli.add_command(populate_database)

    CORS(app)
    initialize_extensions(app)
    register_blueprints(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_revoked(decoded_token):
        return auth.is_token_revoked(decoded_token)

    return app


def initialize_extensions(app):
    """Helper functions"""
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db, directory='migrations')
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth.auth_blueprint)
    app.register_blueprint(contact)
    app.register_blueprint(participants)
