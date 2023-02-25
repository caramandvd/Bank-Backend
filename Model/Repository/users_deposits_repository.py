from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from Model.Domain.users_deposits import UsersDeposits
from Utils.utils import Base, engine


class UsersDepositsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, currency, name, amount, description):
        new_user_deposit = UsersDeposits(
            user_id=user_id,
            currency=currency,
            name=name,
            amount=amount,
            description=description
        )
        self.session.add(new_user_deposit)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id).first()

    def update(self, user_id, description):
        self.session.query(UsersDeposits).filter_by(user_id=user_id, description=description).update({'description': description})
        self.session.commit()

    def delete(self, user_id, name, amount):
        self.session.query(UsersDeposits).filter_by(user_id=user_id, name=name, amount=amount).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersDepositsRepository()
    repo.create('5030329082416', 'RON', 'David', 1200, 'description')
