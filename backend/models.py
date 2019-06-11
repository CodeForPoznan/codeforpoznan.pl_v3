from sqlalchemy import Column
from sqlalchemy.types import Boolean
from sqlalchemy.types import Date
from sqlalchemy.types import DateTime
from sqlalchemy.types import String
from sqlalchemy.types import Integer
from werkzeug.security import generate_password_hash, check_password_hash

from backend.extensions import db


class User(db.Model):
    """User model - for admin."""
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(200), unique=True)
    password = Column(String(100))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


participant_hacknight = db.Table(
    'participant_hacknight',
    db.Column('participant_id', db.Integer, db.ForeignKey('participant.id')),
    db.Column('hacknight_id', db.Integer, db.ForeignKey('hacknight.id'))
)


class Participant(db.Model):
    """Participant model."""
    __tablename__ = 'participant'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(200))
    github = Column(String(200), default="")
    phone = Column(String(13))


class Hacknight(db.Model):
    """Hacknight model."""
    __tablename__ = 'hacknight'
    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(Date)
    participants = db.relationship(
        "Participant",
        secondary=participant_hacknight,
        lazy='subquery',
        backref=db.backref('hacknights', lazy=True)
    )


class JWTToken(db.Model):
    """For purpose of JWT tokens blacklisting"""
    __tablename__ = 'jwt_tokens'
    id = Column(Integer, autoincrement=True, primary_key=True)
    jti = Column(String(36), nullable=False)
    token_type = Column(String(10), nullable=False)
    user_identity = Column(String(200), nullable=False)
    revoked = Column(Boolean, nullable=False)
    expires = Column(DateTime, nullable=False)
