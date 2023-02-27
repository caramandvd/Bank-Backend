from sqlalchemy.orm import sessionmaker
from Model.Domain.users_credentials import UsersCredentials
from Utils.utils import Base, engine


class UsersCredentialsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, username, user_password):

        def hash_password(password):
            import hashlib
            return hashlib.sha256(password.encode('UTF-8')).hexdigest()

        new_user_credentials = UsersCredentials(
            user_id=user_id,
            username=username,
            user_password_hash=hash_password(user_password)
        )
        self.session.add(new_user_credentials)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(UsersCredentials).filter_by(user_id=user_id).first()

    def update(self, user_id, password):
        self.session.query(UsersCredentials).filter_by(user_id=user_id).update(password)
        self.session.commit()

    def delete(self, user_id):
        self.session.query(UsersCredentials).filter_by(user_id=user_id).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersCredentialsRepository()
    repo.create('5030329082416', 'caramandvd', 'password')
    
