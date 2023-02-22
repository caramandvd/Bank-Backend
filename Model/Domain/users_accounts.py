from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey


class UserAccounts(Base):

    __tablename__ = "usersaccounts"
    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey('users.user_id', ondelete="CASCADE"))
    account_number = Column(String(24), foreign_key=ForeignKey('users_accounts.account_number', ondelete="CASCADE"))
    currency = Column(String(3), foreignkey=ForeignKey("currencies.currency", ondelete="CASCADE"))
    amount = Column(Float(2))

    def __repr__(self):
        return f'{self.user_id}; {self.account_number}; {self.currency}; {self.amount}'

    def __str__(self):
        return f'{self.user_id}; {self.account_number}; {self.currency}; {self.amount}'