import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_KEY = 'Something Secret'

    # SQL ALCHEMY DATABASE - Sqlite
    SQL_ALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'vonage.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    DEBUG = True


configs = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
