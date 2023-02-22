from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey


class UsersCards(Base):
    __tablename__ = 'users_cards'
    user_id = Column(String(13), foreign_key=ForeignKey('users.user_id', ondelete="CASCADE"))
    card_number = Column(String(16), primary_key=True, unique=True)
    pin_hash = Column(String(256))
    cvv_hash = Column(String(256))
    expiration_date = Column(Date)
    def __repr__(self):
        return f'{self.__user_id};{self.__card_number};{self.__pin_hash};{self.__cvv_hash};{self.__expiration_date}'

    def __str__(self):
        return f'{self.__user_id};{self.__card_number};{self.__pin_hash};{self.__cvv_hash};{self.__expiration_date}'

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self, cardnumber):
        self.__card_number = cardnumber

    def get_pin_hash(self):
        return self.__pin_hash

    def set_pin_hash(self, pinhash):
        self.__pin_hash = pinhash

    def get_cvv_hash(self):
        return self.__cvv_hash

    def set_cvv_hash(self, cvvhash):
        self.__cvv_hash = cvvhash

    def get_expiration_date(self):
        return self.__expiration_date

    def set_expiration_date(self, expdate):
        self.__expiration_date = expdate
