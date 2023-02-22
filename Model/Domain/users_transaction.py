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
        return f'{self.transaction_id}; {self.user_id}; {self.currency}; {self.amount}; {self.vendor}; {self.date_time}'

    def __str__(self):
        return f'{self.transaction_id}; {self.user_id}; {self.currency}; {self.amount}; {self.vendor}; {self.date_time}'