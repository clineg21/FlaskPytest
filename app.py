from flask import Flask, Blueprint
from flask_restx import Api
from configs.database import db
from configs.ma import ma
from configs.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMYTRACKMODIFICATIONS

from models.models import Account
from schemas.modelschema import AccountSchema
from routes.modelRoutes import account_ns, AccountList

def create_app() -> Flask:
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1/')
    api = Api(blueprint, title="Sample Flask_Restx App")
    app.register_blueprint(blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMYTRACKMODIFICATIONS

    api.add_namespace(account_ns)

    account_ns.add_resource(AccountList, "")

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    create_app().run(port=5000, debug=True)