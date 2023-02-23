from Utils.utils import Base
from sqlalchemy import Column, String, Float, ForeignKey


class UsersAccounts(Base):

    __tablename__ = "users_accounts"
    user_id = Column(String(13), foreign_key=ForeignKey('users.user_id', ondelete="CASCADE"))
    account_number = Column(String(24), primary_key=True, foreign_key=ForeignKey('users_accounts.account_number', ondelete="CASCADE"))
    currency = Column(String(3), foreign_key=ForeignKey('currencies.currency', ondelete="CASCADE"))
    amount = Column(Float(2))

    def __repr__(self):
        return f'{self.user_id}; {self.account_number}; {self.currency}; {self.amount}'

    def __str__(self):
        return f'{self.user_id}; {self.account_number}; {self.currency}; {self.amount}'
