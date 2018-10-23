import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Vars(object):
    IP = 'xxx.xxx.xxx.xxx'
    PORT = '5000'
	
class Timer(object):
    SEG = '90000'
	
class Server(object):
    LINK = '192.168.200.50:18003/soa-infra/services'
	

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