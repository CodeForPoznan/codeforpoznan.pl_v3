import os
from os import urandom


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

    """db config"""
    SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{hostname}:{port}/{databasename}".format(
        username=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        hostname=os.environ.get("DB_HOST"),
        port=5432,
        databasename=os.environ.get("DB_NAME"),
    )
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_recycle": 299}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

    JWT_BLACKLIST_ENABLED = True
