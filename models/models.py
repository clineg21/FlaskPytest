from configs.database import db

class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.Integer, unique=True, nullable=False)
    lName = db.Column(db.String(255), nullable=False)
    client_id = db.Column(db.Integer, nullable=False)