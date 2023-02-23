from Utils.utils import Base
from sqlalchemy import Column, String


class Currencies(Base):
    __tablename__ = "currencies"

    currency = Column(String(3), primary_key=True)

    def __str__(self):
        return f'{self.currency}'

    def __repr__(self):
        return f'{self.currency}'
