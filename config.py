import os

class BaseConfig(object):
    DEBUG =False
    SECRET_KEY = 'dev'


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True