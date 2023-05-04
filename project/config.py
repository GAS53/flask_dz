import os

class Config(object):
    """Base config, uses staging database server."""
    TESTING = False
    DEBUG = False
    DB_SERVER = 'localhost'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dsfgsdfgsdegsre34tg34tg34wergk3jhg34g3q63q4tg3qerg'
    WTF_CSRF_ENABLED = True


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '192.168.19.32'  # переписалть на проде


class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.getcwd()}/db.sqllite'



class TestingConfig(Config):
    DEBUG = True
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'