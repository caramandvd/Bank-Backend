from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Model.Domain.users_transaction import UsersTransactions


class UsersTransactionsRepository:
    def __init__(self):
        engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')
        self.session = sessionmaker(engine)()

    def create(self, user_id, currency, amount, vendor):
        new_user_transaction = UsersTransactions(
            user_id=user_id,
            currency=currency,
            amount=amount,
            vendor=vendor,
            date_time=datetime.now()
        )
        self.session.add(new_user_transaction)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(UsersTransactions).filter_by(user_id=user_id).all()

    def update(self, transaction_id, **kwargs):
        self.session.query(UsersTransactions).filter_by(transaction_id=transaction_id).update(kwargs)
        self.session.commit()

    def delete(self, transaction_id):
        self.session.query(UsersTransactions).filter_by(transaction_id=transaction_id).delete()
        self.session.commit()
