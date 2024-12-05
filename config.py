import os
import random
import string

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

    # Set up the App SECRET_KEY
    SECRET_KEY  = os.getenv('SECRET_KEY', None)
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))    

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # General Config
    FLASK_ENV = os.getenv("FLASK_ENV")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")

    DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
    DB_USERNAME = os.getenv('DB_USERNAME' , None)
    DB_PASS     = os.getenv('DB_PASS'     , None)
    DB_HOST     = os.getenv('DB_HOST'     , None)
    DB_PORT     = os.getenv('DB_PORT'     , None)
    DB_NAME     = os.getenv('DB_NAME'     , None)

    USE_SQLITE  = True 

    # try to set up a Relational DBMS
    if DB_ENGINE and DB_NAME and DB_USERNAME:
        try:
            
            # Relational DBMS: PSQL, MySql
            SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
                DB_ENGINE,
                DB_USERNAME,
                DB_PASS,
                DB_HOST,
                DB_PORT,
                DB_NAME
            ) 
            USE_SQLITE  = False
        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e) )
            print('> Fallback to SQLite ')    

    if USE_SQLITE:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3') 

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'testdb.sqlite3')}"
    
class ProductionConfig(BaseConfig):
    DEBUG = False
    DEBUG_TB_ENABLED = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(BaseConfig):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Testing'   : TestingConfig,
    'Debug'     : DebugConfig
}