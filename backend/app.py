from flask import Flask

from backend.extensions import db, migrate, jwt
from backend.blueprints import auth


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object('backend.config.DevelopmentConfig')

    initialize_extensions(app)
    register_blueprints(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_revoked(decoded_token):
        return is_token_revoked(decoded_token)

    return app


def initialize_extensions(app):
    """Helper functions"""
    db.init_app(app)
    migrate.init_app(app, db, directory='migrations')
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth.auth_blueprint)
