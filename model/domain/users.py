from sqlalchemy import Column, String, Date

from utils.db import Base


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String(13), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    address = Column(String(200), nullable=False)
    phone_number = Column(String(10), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    join_date = Column(Date, nullable=True)

    def __str__(self):
        return f'{self.user_id}; {self.first_name}; {self.last_name}; {self.email}; {self.address}; ' \
               f'{self.phone_number}; {self.date_of_birth}; {self.join_date}\n'

    def __repr__(self):
        return f'{self.user_id}; {self.first_name}; {self.last_name}; {self.email}; {self.address}; ' \
               f'{self.phone_number}; {self.date_of_birth}; {self.join_date}\n'
