import os

basedir = os.path.abspath(os.path.dirname(__file__))
URL = os.getenv('DATABASE_URL')

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = URL
    
class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = URL
