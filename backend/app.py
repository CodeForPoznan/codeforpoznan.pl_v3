from flask import Flask
from flask_cors import CORS

from backend.commands.populate_database import populate_database
from backend.commands.remove_expired_tokens import remove_expired_tokens
from backend.extensions import api, db, mail, migrate, jwt
from backend.models import JWTToken
from backend.resources.auth import (
    UserLogin,
    UserLogout,
    RefreshAccessToken,
    RefreshToken,
)
from backend.resources.contact import SendMessage
from backend.resources.hacknight import (
    HacknightDetails,
    HacknightList,
    HacknightParticipants,
)
from backend.resources.participant import ParticipantDetails, ParticipantsList


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object("backend.config.DevelopmentConfig")
    app.cli.add_command(populate_database)
    app.cli.add_command(remove_expired_tokens)

    CORS(app)
    initialize_extensions(app)

    return app


def initialize_extensions(app):
    """Helper functions"""
    api.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db, directory="migrations")

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        """Checking if token is blacklisted"""
        jti = decrypted_token["jti"]
        return JWTToken.is_jti_blacklisted(jti)


api.add_resource(HacknightList, "/hacknights/")
api.add_resource(HacknightDetails, "/hacknights/<int:id>/")
api.add_resource(HacknightParticipants, "/hacknights/<int:id>/participants/")
api.add_resource(ParticipantDetails, "/participants/<int:id>/")
api.add_resource(ParticipantsList, "/participants/")
api.add_resource(RefreshAccessToken, "/auth/refresh/")
api.add_resource(RefreshToken, "/auth/refresh-token/")
api.add_resource(SendMessage, "/send-email/")
api.add_resource(UserLogin, "/auth/login/")
api.add_resource(UserLogout, "/auth/logout/")
