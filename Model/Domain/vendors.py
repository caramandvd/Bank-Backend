from sqlalchemy import Column, String, Date, BigInteger

from utils.db import Base


class Vendors(Base):
    __tablename__ = "vendors"

    vendor_id = Column(BigInteger, primary_key=True, autoincrement=True)
    vendor_name = Column(String(40), nullable=False)
    email = Column(String(50), nullable=False)
    address = Column(String(40), nullable=False)
    phone_number = Column(String(10), nullable=False)
    join_date = Column(Date, nullable=True)

    def __str__(self):
        return f'{self.vendor_id}; {self.vendor_name}; {self.email}; {self.address}; {self.phone_number}; ' \
               f'{self.join_date}'

    def __repr__(self):
        return f'{self.vendor_id}; {self.vendor_name}; {self.email}; {self.address}; {self.phone_number}; ' \
               f'{self.join_date}'
