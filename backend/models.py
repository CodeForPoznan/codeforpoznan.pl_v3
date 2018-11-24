from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Boolean

#from app import db


class User(db.Model):
    """
    User model - for admin
    """
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(20), unique=True)
    hashed_password = Column(String(100))

    def get_id(self):
        return str(self.id)

    def get(self):
        return self


class Participant(db.Model):
    """
    Participant model
    """
    __tablename__ = 'participant'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(30), default="")
    github = Column(String(200), default="")
    phone = Column(Integer, default=0 )

    def get_id(self):
        return str(self.id)

    def get(self):
        return self



class Hacknight(db.Model):
    """
    Hacknight model
    """
    __tablename__ = 'hacknight'
    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(String(20))

    def get(self):
        return self
