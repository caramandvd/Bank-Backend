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
        return f'{self.user_id};{self.currency};{self.name};{self.amount};{self.description}'

    def __repr__(self):
        return f'{self.user_id};{self.currency};{self.name};{self.amount};{self.description}'