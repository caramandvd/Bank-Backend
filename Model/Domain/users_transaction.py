from xmlrpc.client import DateTime

from Utils.utils import Base
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey


class UsersTransactions(Base):

    __tablename__ = "users_transactions"

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(13), foreign_key=ForeignKey("users.user_id", ondelete="CASCADE"))
    currency = Column(String(3), foreign_key=ForeignKey("currencies.currency", ondelete="CASCADE"))
    amount = Column(Float(2))
    vendor = Column(String(100))
    date_time = Column(DateTime)

    def __repr__(self):
        return f'{self.__transaction_id};{self.__user_id};{self.__currency};{self.__amount};{self.__vendor};' \
               f'{self.__date_time}'

    def __str__(self):
        return f'{self.__transaction_id};{self.__user_id};{self.__currency};{self.__amount};{self.__vendor};' \
               f'{self.__date_time}'

    def get_transaction_id(self):
        return self.__transaction_id

    def set_transaction_id(self, id_transactie):
        self.__transaction_id = id_transactie

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, id_transactie):
        self.__transaction_id = id_transactie

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_vendor(self):
        return self.__vendor

    def set_vendor(self, vendor):
        self.__vendor = vendor

    def get_date_time(self):
        return self.__date_time

    def set_date_time(self, date_time):
        self.__date_time = date_time