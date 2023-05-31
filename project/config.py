import os

class Config(object):
    """Base config, uses staging database server."""
    TESTING = False
    DEBUG = False
    DB_SERVER = 'localhost'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dsfgsdfgsdegsre34tg34tg34wergk3jhg34g3q63q4tg3qerg'
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = 'dpg-chrib0rhp8ud4n6mlfg0-a'
    SQLALCHEMY_DATABASE_URI = 'postgres://im_user:V8orqf2qaZsQ3pjYKPJFh7s9wqAA8mP6@dpg-chrib0rhp8ud4n6mlfg0-a.ohio-postgres.render.com/db_50m4'



class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.getcwd()}/db.sqllite'



class TestingConfig(Config):
    DEBUG = True
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'