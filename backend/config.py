import os

from backend.helpers import ask_for_temporary_mail


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
    DB_PORT = os.environ["DB_PORT"]
    DB_NAME = os.environ["DB_NAME"]
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_recycle": 299}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """jwt config"""
    JWT_BLACKLIST_ENABLED = True

    """mail config"""
    MAIL_DEBUG = True  # always on, for error checking
    MAIL_USE_TLS = True  # always on, for security
    MAIL_USE_SSL = False  # always off, default
    MAIL_WEB_URL = ""  # used only for ethereal.mail

    MAIL_SUPPRESS_SEND = os.environ["MAIL_SUPPRESS_SEND"].lower() == "true"
    MAIL_USERNAME = os.environ["MAIL_USERNAME"]
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    MAIL_PORT = os.environ["MAIL_PORT"]

    def __init__(self):
        self.init_mail_variables()

    @classmethod
    def init_mail_variables(cls):
        if cls.MAIL_SUPPRESS_SEND:
            print("Suppression of sending outgoing mails is enabled")
            print("Disabling email support. Emails will NOT be sent\n" * 3)
            return

        if cls.MAIL_USERNAME and cls.MAIL_PASSWORD:
            print("Using environment variables for email support")
            print("Watch logs for links with received messages")
            return

        if data := ask_for_temporary_mail():
            print("Using temporary mailing account for email support")
            print("Watch logs for links with received messages")
            cls.MAIL_WEB_URL = data["MAIL_WEB_URL"]
            cls.MAIL_USERNAME = data["MAIL_USERNAME"]
            cls.MAIL_PASSWORD = data["MAIL_PASSWORD"]
            cls.MAIL_SERVER = data["MAIL_SERVER"]
            cls.MAIL_PORT = data["MAIL_PORT"]
            return

        # dead config's switch - everything else failed, block mails
        print("Failed to initialize temporary mailing account!")
        print("Disabling email support. Emails will NOT be sent\n" * 3)
        cls.MAIL_SUPPRESS_SEND = True


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
