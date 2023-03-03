from model.repository.users_credentials_repository import UsersCredentialsRepository
from utils.db import engine, Base
from model.repository.users_credentials_repository import hash_password


class UsersCredentialsController:
    def __init__(self, users_credentials_repository):
        self.users_credentials_repository = users_credentials_repository

    def hash_password(password):
        import hashlib
        return hashlib.sha256(password.encode('UTF-8')).hexdigest()

    def add_username_password(self, user_id, username, user_password_unhashed):
        UsersCredentialsRepository().create(user_id=user_id, username=username,
                                            user_password=hash_password(user_password_unhashed))

    def update_password(self, user_id, new_password_unhashed):
        UsersCredentialsRepository().update(user_id=user_id, new_password=new_password_unhashed)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersCredentialsController(UsersCredentialsRepository())
    # repo.create_user('5090909983456', 'Andreiucu', 'Pope', 'andrei@mail.com', 'Biblioteca', '0711223344')
    # repo.add_username_password('5030304123456', 'Alex', 'Radu')
    repo.update_password('5030329082416', '0066')
