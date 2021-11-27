from decouple import config

class Config:
    DEBUG=False
    CSRF_ENABLED=True
    # SQLALCHEMY_DATABASE_URI=config('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI='DATABASE_URL'
    SQLALCHEMY_TRACK_MODIFICTIONS=False

class DevelopmentConfig(Config):
    DEBUG=False

class TestingConfig(Config):
    TESTING=True
    # SQLALCHEMY_DATABASE_URI=config('DATABASE_TEST_URL')
    SQLALCHEMY_DATABASE_URI='HEROKU_POSTGRESQL_GRAY_URL'
    # DEBUG=True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
