from datetime import datetime, date

from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker

from model.domain.users import Users
from utils.db import Base, engine
from utils.exc import InvalidUserID


class UsersRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, first_name, last_name, email_name, address, phone_number):

        def get_date_of_birth(user_id):
            centuries = {
                '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000}
            year = int(user_id[1:3]) + centuries.get(user_id[0], 1900)
            month = int(user_id[3:5])
            day = int(user_id[5:7])
            try:
                return date(year, month, day)
            except ValueError:
                raise InvalidUserID()

        new_user = Users(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email_name=email_name,
            address=address,
            phone_number=phone_number,
            date_of_birth=get_date_of_birth(user_id=user_id),
            join_date=datetime.now()
        )
        self.session.add(new_user)
        self.session.commit()

        if self.session.query(UsersRepository).filter_by(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                email_name=email_name,
                address=address,
                phone_number=phone_number
        ).first():
            print("Successfully inserted new user into the database.")
            return True
        else:
            print("Error: Failed to insert new user into the database.")
            return False

    def read(self, user_id):
        return self.session.query(Users).filter_by(user_id=user_id).first()

    def update(self, user_id, **kwargs):
        print(kwargs)
        self.session.query(Users).filter_by(user_id=user_id).update(kwargs)
        self.session.commit()

    def delete(self, user_id):
        self.session.query(Users).filter_by(user_id=user_id).delete()
        self.session.commit()

    def read_all(self):
        return self.session.query(Users).all()

    def get_email_by_user_id(self, user_id):
        user = self.session.query(Users).filter_by(user_id=user_id).first()
        if user:
            return user.email_name

        return None


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersRepository()
    repo.create('5070404123456', 'Luca', 'Caraman', 'luca@mail.com', 'Camera lui', '0712341234')
