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
        return f'{self.user_id};{self.card_number};{self.pin_hash};{self.cvv_hash};{self.expiration_date}'

    def __str__(self):
        return f'{self.user_id};{self.card_number};{self.pin_hash};{self.cvv_hash};{self.expiration_date}'