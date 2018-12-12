from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User model - for admin."""
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(200), unique=True)
    password = Column(String(100))


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
    date = Column(Date(20))
