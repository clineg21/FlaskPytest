from Flask_Pytest.configs.ma import ma
from Flask_Pytest.models.models import *

class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Account
        load_instance=True