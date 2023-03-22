from datetime import datetime
from pprint import pprint

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from model.domain.users import Users
from model.domain.users_transaction import UsersTransactions
from model.domain.vendors import Vendors
from utils.db import engine, Base


class UsersTransactionsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def add_user_transaction(self, user_id, currency, amount, receiver_id):
        if self.session.query(Users).filter_by(user_id=receiver_id).first():
            pass
        elif self.session.query(Vendors).filter_by(vendor_id=receiver_id).first():
            print('User exists')
        else:
            print('User does not exist!')
            return None
        new_user_transaction = UsersTransactions(
            user_id=user_id,
            currency=currency,
            amount=amount,
            receiver_id=receiver_id,
            date_time=datetime.now()
        )
        self.session.add(new_user_transaction)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(UsersTransactions).filter_by(user_id=user_id).all()

    def read_all_transactions_by_id(self, user_id):
        subquery = self.session.query(func.max(UsersTransactions.transaction_id)). \
            group_by(UsersTransactions.vendor).subquery()
        return self.session.query(UsersTransactions). \
            filter(user_id=user_id). \
            filter(UsersTransactions.transaction_id.in_(subquery)).all()

    def update(self, transaction_id, **kwargs):
        self.session.query(UsersTransactions).filter_by(transaction_id=transaction_id).update(kwargs)
        self.session.commit()

    def delete(self, transaction_id):
        self.session.query(UsersTransactions).filter_by(transaction_id=transaction_id).delete()
        self.session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    repo = UsersTransactionsRepository()
