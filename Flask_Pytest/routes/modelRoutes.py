from flask_restx import Resource, fields, Namespace
from flask import request, jsonify
from Flask_Pytest.configs.database import db

from Flask_Pytest.models.models import Account
from Flask_Pytest.schemas.modelschema import AccountSchema

account_ns = Namespace('accounts', description="Account APIs")

account_schema = AccountSchema(many=True)
create_account_schema = AccountSchema()

account = account_ns.model('Account', {
    'account_number': fields.Integer('Account #'),
    'lName': fields.String('Last name of the account user'),
    'client_id': fields.Integer('id of the client')
})

class AccountList(Resource):
    @account_ns.doc('get account data')
    def get(self):
        return account_schema.dump(Account.query.all()), 200

    @account_ns.expect(account)
    @account_ns.doc('Create a new account')
    def post(self):
        account_json = request.get_json()
        newAccount = Account(account_number=account_json['account_number'], lName=account_json['lName'], client_id=account_json['client_id'])
        db.session.add(newAccount)
        db.session.commit()
        return create_account_schema.dump(newAccount), 201