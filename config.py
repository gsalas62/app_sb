import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Vars(object):
    IP = '172.20.10.35'
    PORT = '5000'
	
class Timer(object):
    SEG = '60000'
	

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '123dasdasdg3sd21as-11slk'
    
class ProductionConfig(Config):
    DEBUG = False
	
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
	
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
	
class TestingConfig(Config):
    TESTING = True