from model.repository.users_repository import UsersRepository
from utils.db import engine, Base


class UsersController:
    def __init__(self, users_repository):
        self.users_repository = users_repository

    def create_user(self, user_id, first_name, last_name, email, address, phone_number):
        self.users_repository.create(user_id=user_id, first_name=first_name, last_name=last_name, email=email,
                                     address=address, phone_number=phone_number)

    def get_user_by_id(self, user_id):
        return UsersRepository().read_user_by_user_id(user_id=user_id)

    def get_user_by_phone_nr(self, phone_number):
        return UsersRepository().read_user_by_phone_number(phone_number=phone_number)

    def get_user_by_email(self, email):
        return UsersRepository().read_user_by_email(email)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersController(UsersRepository())
    # repo.create_user('5090909983456', 'Andreiucu', 'Pope', 'andrei@mail.com', 'Biblioteca', '0711223344')
    print(repo.get_user_by_email('melimese@gmail.com'))
    print(repo.get_user_by_phone_nr('0755925361'))
    print(repo.get_user_by_id('5030329082416'))
    print(repo.get_user_by_email('luca@mail.com'))
    print(repo.get_user_by_id('5030304123456'))
    # repo.create_user('5090909083480', 'Ghita3', 'Malone3', 'ghita3@mail.com', 'Bucium', '0710923344')
