class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    """flask_mail configuration required in production env"""
    MAIL_SERVER = None
    MAIL_PORT = None
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_USE_TLS = None
    MAIL_USE_SSL = None
    MAIL_ASCII_ATTACHMENTS = None


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    TESTING = True
