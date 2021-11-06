import os

from flask import Flask, Blueprint
from flask_restx import Api
from configs.database import db
from configs.ma import ma
from configs.config import SQLALCHEMYTRACKMODIFICATIONS
from decouple import config
from routes.modelRoutes import account_ns, AccountList
from instance.instanceconf import app_config

def create_app(config_name) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('instanceconf.py')
    db.init_app(app)
    ma.init_app(app)
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1/')
    api = Api(blueprint, title="Sample Flask_Restx App")
    app.register_blueprint(blueprint)
    # app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMYTRACKMODIFICATIONS

    api.add_namespace(account_ns)

    account_ns.add_resource(AccountList, "")

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    config_name = os.getenv('APP_SETTINGS')
    print(config_name)
    create_app(config_name).run(port=5000, debug=True)