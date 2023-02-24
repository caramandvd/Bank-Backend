from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from Model.Domain.users_accounts import UsersAccounts
from Utils.utils import engine, Base


class UsersAccountsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, account_number, currency, amount):
        if amount > 0:
            new_user_account = UsersAccounts(
                user_id=user_id,
                account_number=account_number,
                currency=currency,
                amount=amount
            )
            self.session.add(new_user_account)

            if self.session.query(UsersAccounts).filter_by(user_id=user_id, account_number=account_number).first():
                print("Successfully inserted new user account into the database.")
                return True
            else:
                print("Error: Failed to insert new user account into the database.")
                return False
        else:
            print("Error: Amount must be greater than 0.")
            return False


    def read(self, user_id):
        return self.session.query(UsersAccounts).filter_by(user_id=user_id).first()

    def update(self, user_id, amount):
        if amount:
            self.session.query(UsersAccounts).filter_by(user_id=user_id).update({'amount': amount})
            self.session.commit()

    def delete(self, user_id):
        self.session.query(UsersAccounts).filter_by(user_id=user_id).delete()
        self.session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersAccountsRepository()
    repo.create('6020528123456', 'EURFASDFASDFASDFASDPAVMM', 'CZK', 1234)

