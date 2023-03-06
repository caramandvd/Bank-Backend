from model.repository.users_credentials_repository import UsersCredentialsRepository
from model.repository.users_repository import UsersRepository
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


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    repo = AppController(UsersRepository())
    repo.add_user('4080808121216', 'Ghi', 'Aur', 'ghi@mail.com', 'CJ', '0799911122', 'ghgh', 'nam')