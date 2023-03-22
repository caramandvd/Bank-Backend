from pprint import pprint

from model.repository.users_credentials_repository import UsersCredentialsRepository
from model.repository.users_repository import UsersRepository
from model.repository.users_transaction_repository import UsersTransactionsRepository
from model.repository.vendors_repository import VendorsRepository
from utils.db import Base, engine


class AppController:
    def __init__(self, users_repository):
        self.users_repository = users_repository

    def create_user(self, user_id, first_name, last_name, email, address, phone_number):
        self.users_repository.create(user_id=user_id, first_name=first_name, last_name=last_name, email=email,
                                     address=address, phone_number=phone_number)

    def get_user_by_id(self, user_id):
        return UsersRepository().read_user_by_user_id(user_id=user_id)

    def get_user_by_email(self, email):
        return UsersRepository().read_user_by_email(email=email)

    def get_user_by_phone_nr(self, phone_number):
        return UsersRepository().read_user_by_phone_number(phone_number=phone_number)

    def add_username_password(self, user_id, username, user_password_hash):
        UsersCredentialsRepository().create(user_id, username, user_password_hash)

    def update_password(self, user_id, new_user_password_hash):
        UsersCredentialsRepository().update(user_id, new_user_password_hash)

    def add_user(self, user_id, first_name, last_name, email, address, phone_number, username, user_password_hash):
        self.users_repository.create(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            phone_number=phone_number
        )
        self.add_username_password(user_id=user_id, username=username, user_password_hash=user_password_hash)

    def get_last_transactions_by_user_id(self, user_id):
        repo = UsersTransactionsRepository()
        transactions = repo.read(user_id)
        result = {}
        for transaction in transactions:
            if transaction.receiver_id[:3] != "100":
                result[transaction.receiver_id] = {
                    "receiver_username": UsersCredentialsRepository().get_username_by_user_id(transaction.receiver_id),
                    "currency": transaction.currency,
                    "amount": transaction.amount,
                    "date_time": transaction.date_time.isoformat()
                }
            else:
                result[transaction.receiver_id] = {
                    "receiver_username": VendorsRepository().return_vendor_name_by_id(transaction.receiver_id),
                    "currency": transaction.currency,
                    "amount": transaction.amount,
                    "date_time": transaction.date_time.isoformat()
                }
        return result


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    repo = AppController(UsersRepository())
    pprint(repo.get_last_transactions_by_user_id('5030329082416'))
