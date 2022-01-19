from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import Boolean, Date, DateTime, Integer, String, Text
from werkzeug.security import generate_password_hash, check_password_hash

from backend.extensions import db


class User(db.Model):
    """User model - for admin."""

    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(200), unique=True)
    password = Column(String(100))
    skills = db.relationship("UserSkill", back_populates="user")

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserSkill(db.Model):
    """Association tabale between user and techstack models."""

    __tablename__ = "user_skill"
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    techstack_id = Column(ForeignKey("techstack.id"), primary_key=True)
    skill_level = Column(Integer)
    is_learning_goal = Column(Boolean, default=False)
    skill = db.relationship("TechStack", back_populates="users")
    user = db.relationship("User", back_populates="skills")


participant_hacknight = db.Table(
    "participant_hacknight",
    db.Column("participant_id", db.Integer, db.ForeignKey("participant.id")),
    db.Column("hacknight_id", db.Integer, db.ForeignKey("hacknight.id")),
)


class Participant(db.Model):
    """Participant model."""

    __tablename__ = "participant"
    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    github = Column(String(200), unique=True, nullable=False)
    phone = Column(String(13))
    slack = Column(String(21))


class Hacknight(db.Model):
    """Hacknight model."""

    __tablename__ = "hacknight"
    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(Date, nullable=False, unique=True)
    participants = db.relationship(
        "Participant",
        secondary=participant_hacknight,
        lazy="subquery",
        backref=db.backref("hacknights", lazy=True),
    )


participant_team = db.Table(
    "participant_team",
    db.Column("participant_id", db.Integer, db.ForeignKey("participant.id")),
    db.Column("team_id", db.Integer, db.ForeignKey("team.id")),
)

team_techstack = db.Table(
    "team_techstack",
    db.Column("team_id", db.Integer, db.ForeignKey("team.id")),
    db.Column("techstack_id", db.Integer, db.ForeignKey("techstack.id")),
)


class Team(db.Model):
    """Team model."""

    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    project_name = Column(String(50), nullable=False, unique=True)
    description = Column(Text)
    project_url = Column(String(200), unique=True)
    members = db.relationship(
        "Participant",
        secondary=participant_team,
        lazy="subquery",
        backref=db.backref("teams", lazy=True),
    )
    tech_stack = db.relationship(
        "TechStack",
        secondary=team_techstack,
        lazy="subquery",
        backref=db.backref("teams", lazy=True),
    )


class TechStack(db.Model):
    """TechStack model."""

    __tablename__ = "techstack"
    id = Column(Integer, primary_key=True)
    technology = Column(String(50), nullable=False, unique=True)
    label = Column(String(50))
    users = db.relationship("UserSkill", back_populates="skill")


class JWTToken(db.Model):
    """For purpose of JWT tokens blacklisting."""

    __tablename__ = "jwt_tokens"
    id = Column(Integer, autoincrement=True, primary_key=True)
    jti = Column(String(36), nullable=False)
    token_type = Column(String(10), nullable=False)
    user_identity = Column(String(200), nullable=False)
    revoked = Column(Boolean, nullable=False)
    expires = Column(DateTime, nullable=False)

    @classmethod
    def is_jti_blacklisted(cls, jti):
        try:
            token = cls.query.filter_by(jti=jti).one()
            return token.revoked
        except NoResultFound:
            return True

    def expired(self):
        return datetime.now() > self.expires

    @classmethod
    def remove_expired(cls):
        for token in cls.query.all():
            if token.expired():
                db.session.delete(token)
        db.session.commit()
