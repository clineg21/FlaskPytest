from configs.ma import ma
from models.models import *

class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Account
        load_instance=True