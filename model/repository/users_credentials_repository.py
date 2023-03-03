from sqlalchemy.orm import sessionmaker
from model.domain.users_credentials import UsersCredentials
from utils.db import Base, engine

def hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode('UTF-8')).hexdigest()


class UsersCredentialsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, username, user_password):

        new_user_credentials = UsersCredentials(
            user_id=user_id,
            username=username,
            user_password_hash=hash_password(user_password)
        )
        self.session.add(new_user_credentials)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(UsersCredentials).filter_by(user_id=user_id).first()

    def update(self, user_id, new_password):
        user_credentials = self.read(user_id)
        if user_credentials is not None:
            user_credentials.user_password_hash = hash_password(new_password)
            self.session.commit()
        else:
            raise ValueError(f"User with id {user_id} does not exist.")

    def delete(self, user_id):
        self.session.query(UsersCredentials).filter_by(user_id=user_id).delete()
        self.session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersCredentialsRepository()
    repo.create('5030329082416', 'caramandvd', 'password')
