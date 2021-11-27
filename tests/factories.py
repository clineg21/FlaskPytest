import factory
from faker import Faker
import sqlalchemy
from factory.alchemy import SQLAlchemyModelFactory
from Flask_Pytest.models.models import Account
from Flask_Pytest.configs.database import db

class AccountFactory(SQLAlchemyModelFactory):
    class Meta:
        model=Account
        sqlalchemy_session = db.session

    account_number = factory.Faker('random_number')
    lName = factory.Faker('name')
    client_id = factory.Faker('random_number')