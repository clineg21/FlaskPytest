from decouple import config
import os
import psycopg2

class Config:
    DEBUG=False
    CSRF_ENABLED=True
    # SQLALCHEMY_DATABASE_URI=config('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
    conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI, sslmode='require')
    SQLALCHEMY_TRACK_MODIFICTIONS=False

class DevelopmentConfig(Config):
    DEBUG=False

class TestingConfig(Config):
    TESTING=True
    # SQLALCHEMY_DATABASE_URI=config('DATABASE_TEST_URL')
    # SQLALCHEMY_DATABASE_URI='HEROKU_POSTGRESQL_GRAY_URL'
    SQLALCHEMY_DATABASE_TEST_URI = os.environ['HEROKU_POSTGRESQL_GRAY_URL']
    conn = psycopg2.connect(SQLALCHEMY_DATABASE_TEST_URI, sslmode='require')
    # DEBUG=True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
