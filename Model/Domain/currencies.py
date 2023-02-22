from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, Double


class Currencies(Base):
    __tablename__ = "currencies"

    currency = Column(String(3), primary_key=True)

    def __str__(self):
        return f'{self.__currency}'

    def __repr__(self):
        return f'{self.__currency}'

    def set_currencies(self, currency):
        self.__currency = currency

    def get_currencies(self):
        return self.__currency