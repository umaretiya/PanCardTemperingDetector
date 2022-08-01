import os


class Config(object):
    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    # print(basedir)
    
    SECRET_KEY= 'pianalytix'
    
    DB_NAME="production-db"
    DB_UERNAME='root'
    DB_PASSWORD = 'pianalytix'
    
    UPLOADS = "/home/username/app/app/static/uploads"
    
    SESSION_COOCKIE_SECURE = None
    DEFAULT_THEME = None 
 
 
class ProductionConfig(Config):
    pass    
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_NAME = "production-db"
    DB_UERNAME = "root"
    DB_PASSWORD = 'pianalytix'
    
    UPLOADS = "/home/username/app/app/static/uploads"
    SESSION_COOCKIE_SECURE = False 
    
    
class TestingConfig(Config):
    DEBUG = True
    
    DB_NAME = "production-db"
    DB_UERNAME = "root"
    DB_PASSWORD = 'pianalytix'
    
    UPLOADS = "/home/username/app/app/static/uploads"
    SESSION_COOCKIE_SECURE = False 


class DebugConfig(Config):
    DEBUG = False
