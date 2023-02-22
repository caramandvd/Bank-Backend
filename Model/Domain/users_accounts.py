from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey


class UserAccounts(Base):

    __tablename__ = "usersaccounts"
    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey('users.user_id', ondelete="CASCADE"))
    account_number = Column(String(24), foreign_key=ForeignKey('users_accounts.account_number', ondelete="CASCADE"))
    currency = Column(String(3), foreignkey=ForeignKey("currencies.currency", ondelete="CASCADE"))
    amount = Column(Float(2))

    def __repr__(self):
        return f'{self.__user_id};{self.__account_number};{self.__currency};{self.__amount}'

    def __str__(self):
        return f'{self.__user_id};{self.__account_number};{self.__currency};{self.__amount}'

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount
