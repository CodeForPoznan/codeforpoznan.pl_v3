from flask import Flask
from flask_cors import CORS

from backend.commands.populate_database import populate_database
from backend.extensions import api, db, mail, migrate, jwt
from backend.resources.auth import UserLogin, UserLogout
from backend.resources.contact import SendMessage
from backend.resources.hacknight import HacknightList
from backend.resources.participant import ParticipantsList


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object('backend.config.DevelopmentConfig')
    app.cli.add_command(populate_database)

    CORS(app)
    initialize_extensions(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_revoked(decoded_token):
        return auth.is_token_revoked(decoded_token)

    return app


def initialize_extensions(app):
    """Helper functions"""
    api.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db, directory='migrations')
    jwt.init_app(app)


api.add_resource(UserLogin, "/auth/login")
api.add_resource(UserLogout, "/auth/logout")
api.add_resource(SendMessage, "/send-email/")
api.add_resource(ParticipantsList, "/participants/")
api.add_resource(HacknightList, "/hacknights/")
