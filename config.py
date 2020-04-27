"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = True
    DEBUG = True


    # Database
#    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://zoe:Passmy1!@127.0.0.1:3306/STUDENT_SYSTEM'
    SQLALCHEMY_USERNAME = 'zoe'
    SQLALCHEMY_PASSWORD = 'Password'
    SQLALCHEMY_DATABASE_NAME = 'STUDENT_SYSTEM'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PROPAGATE_EXCEPTION = True

    # JWT
    SECRET_KEY = 'my_key'
    JWT_BLACKLIST_ENABLE = True
    JWT_BLACKLIST_TOKEN_CHECKS = [
        "access",
        "refresh",
    ]



class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URI')