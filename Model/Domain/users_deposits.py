from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, Double


class UsersDeposits(Base):
    __tablename__ = 'users_deposits'
    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey("users.user_id", ondelete="CASCADE"))
    currency = Column(String(3), foreign_key=ForeignKey('currencies.currency', ondelete="CASCADE"))
    name = Column(String(30))
    amount = Column(Float(2))
    description = Column(String)
    def __str__(self):
        return f'{self.__user_id};{self.__currency};{self.__name};{self.__amount};{self.__description}'

    def __repr__(self):
        return f'{self.__user_id};{self.__currency};{self.__name};{self.__amount};{self.__description}'

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description