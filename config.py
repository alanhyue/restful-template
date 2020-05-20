import os

basedir = os.path.dirname(__file__)
LOUD_ENV_GET = os.environ.get('LOUD_ENV_GET', '0')

def env_get(key, default=None):
    if LOUD_ENV_GET == '1':
        return loud_env_get(key, default)
    else:
        return os.environ.get(key, default)

def loud_env_get(key, default=None):
    value = os.environ.get(key, default)
    if key in os.environ:
        print(f"Env Var: {key} = {value}")
    else:
        print(f"Env Var: {key} not found.")
    return value


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_STATIC_FOLDER = "../eagleeye/dist/"
    FLASK_TEMPLATE_FOLDER = "../eagleeye/dist/"


class DevelopmentConfig(Config):
    DEVELOPMENT = True

    SQLALCHEMY_DATABASE_URI = env_get('SQLALCHEMY_DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    

class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = env_get('SQLALCHEMY_TEST_DATABASE_URI') or \
        'sqlite://'
    DATA_FILES_URI = env_get('DATA_FILES_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = env_get('SQLALCHEMY_DATABASE_URI')
    DATA_FILES_URI = env_get('DATA_FILES_URL')

config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig(),
    'default': DevelopmentConfig(),
}
