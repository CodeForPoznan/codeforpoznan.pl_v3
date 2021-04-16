import os
import logging

import requests


class Config:
    """
    Default config context.
    """

    """app config"""
    DEBUG = True
    TESTING = True

    SECRET_KEY = os.environ["SECRET_KEY"]
    BASE_URL = os.environ["BASE_URL"]

    """db config"""
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"] or 5432
    DB_NAME = os.environ["DB_NAME"]
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_recycle": 299}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_BLACKLIST_ENABLED = True

    """mail config"""
    MAIL_SUPPRESS_SEND = False  # always off, never block mail sending
    MAIL_DEBUG = True  # always on, needed for error checking
    MAIL_USE_TLS = True  # always on, for security (TM)
    MAIL_USE_SSL = False  # always off, for security (TM)
    MAIL_WEB_SERVER = None  # defaults to empty, might be set later
    MAIL_RECIPIENT = "hello@codeforpoznan.pl"

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # empty MAIL_* vars are a hint that we should use the temporary account
    if not MAIL_SERVER:
        json = {"requestor": "nodemailer", "version": "6.5.0"}
        resp = requests.post("https://api.nodemailer.com/user", json=json)
        if resp.status_code == 200:
            data = resp.json()
            MAIL_SERVER = data["smtp"]["host"]
            MAIL_PORT = data["smtp"]["port"]
            MAIL_USERNAME = data["user"]
            MAIL_PASSWORD = data["pass"]
            MAIL_WEB_SERVER = data["web"]
            logging.info(
                "Using temporary mailing account for email support."
                "Watch logs for links with received messages"
            )

    # fail-safe switch in case anything failed above
    if not MAIL_SERVER:
        MAIL_SUPPRESS_SEND = True
        logging.warning(
            "Failed to initialize temporary mailing account! "
            "Disabling email support. Emails will not be sent"
        )


class ProductionConfig(Config):
    """
    Used for https://codeforpoznan.pl/ (AWS Lambda)
    """

    pass


class StagingConfig(Config):
    """
    Used for https://dev.codeforpoznan.pl/ (AWS Lambda)
    """

    pass


class DevelopmentConfig(Config):
    """
    Used for https://localhost:8088/ (Docker)
    """

    pass
