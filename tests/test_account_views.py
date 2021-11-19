import json
# from .factories import AccountFactory
from Flask_Pytest.models.models import Account
from Flask_Pytest.configs.database import db

def test_user_can_retrieve_empty_list_account(client, db):
    response = client.get('/api/v1/accounts')
    response_body = response.get_json()
    assert response.status == '200 OK'
    assert len(response_body) == 0

def test_user_can_create_an_account(client, db):
    account = {
        "id": 1,
        "account_number": 1234,
	     "lName": "Mills",
	     "client_id": 1
	     }
    response = client.post('/api/v1/accounts', json=account,)
    assert response.status == '201 CREATED'
    print(account)
    print(response.get_json())
    assert response.get_json() == account
    assert response.json['account_number'] == 1234
    assert response.json['lName'] == "Mills"
    assert Account.query.all() != 0