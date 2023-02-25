from datetime import datetime, timedelta
import hashlib
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from Model.Domain.users_cards import UsersCards
from Utils.utils import Base, engine


def hash_pin(unhased_pin):
    return hashlib.sha256(unhased_pin.encode('UTF-8')).hexdigest()


def hash_cvv(unhased_cvv):
    return hashlib.sha256(unhased_cvv.encode('UTF-8')).hexdigest()


def create_expiration_date_for_card():
    current_date = datetime.now()
    expiration_date = current_date + timedelta(days=1095)  # 1095 days = 3 years

    expiration_month = expiration_date.month
    expiration_year = expiration_date.year % 100  # We only need the last two digits of the year

    return "{:02d}/{:02d}".format(expiration_month, expiration_year)


class UsersCardsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, card_number, unhased_pin, unhased_cvv):
        new_user_card = UsersCards(
            user_id=user_id,
            card_number=card_number,
            pin_hash=hash_pin(unhased_pin=unhased_pin),
            cvv_hash=hash_cvv(unhased_cvv=unhased_cvv),
            expiration_date=create_expiration_date_for_card()
        )

        self.session.add(new_user_card)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(UsersCards).filter_by(user_id=user_id).first()

    def update(self, user_id, card_number, new_unhashed_pin):
        self.session.query(UsersCards).filter_by(user_id=user_id, card_number=card_number).update({'pin_hash': hash_pin(new_unhashed_pin)})
        self.session.commit()

    def delete(self, card_number):
        self.session.query(UsersCards).filter_by(card_number=card_number).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersCardsRepository()
    # repo.create('5030329082416', '1234567890123456', '1234', '111')
    repo.create('6020528123456', '2234567890123456', '5678', '100')
    repo.create('5070404123456', '3234567890123456', '1122', '171')
    # print(repo.read('5030329082416'))
    # repo.update('5030329082416', '1234567890163458', '2345')
    # repo.delete('1234567890163458')
