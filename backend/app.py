from flask import Flask

from backend.extensions import db, migrate


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object('backend.config.DevelopmentConfig')

    initialize_extensions(app)

    return app


def initialize_extensions(app):
    """Helper functions"""
    db.init_app(app)
    migrate.init_app(app, db, directory='migrations')
