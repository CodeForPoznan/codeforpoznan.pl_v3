import os

from flask import Flask
from flask_cors import CORS
from werkzeug.utils import import_string

from backend.commands.populate_database import populate_database
from backend.commands.import_attendance_list import import_attendance_list
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
from backend.resources.team import TeamDetails, TeamList, TeamMembers


def create_app():
    """Application factory function"""
    app = Flask(__name__)

    # create config class instance and init config from it
    env = os.environ["FLASK_ENV"].title()
    cls = import_string(f"backend.config.{env}Config")
    app.config.from_object(cls())

    app.cli.add_command(populate_database)
    app.cli.add_command(remove_expired_tokens)
    app.cli.add_command(import_attendance_list)

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


api.add_resource(HacknightList, "/api/hacknights/")
api.add_resource(HacknightDetails, "/api/hacknights/<int:id>/")
api.add_resource(HacknightParticipants, "/api/hacknights/<int:id>/participants/")
api.add_resource(ParticipantDetails, "/api/participants/<int:id>/")
api.add_resource(ParticipantsList, "/api/participants/")
api.add_resource(RefreshAccessToken, "/api/auth/refresh/")
api.add_resource(RefreshToken, "/api/auth/refresh-token/")
api.add_resource(SendMessage, "/api/send-email/")
api.add_resource(UserLogin, "/api/auth/login/")
api.add_resource(UserLogout, "/api/auth/logout/")
api.add_resource(TeamList, "/api/teams/")
api.add_resource(TeamDetails, "/api/teams/<int:id>/")
api.add_resource(TeamMembers, "/api/teams/<int:id>/members/")
