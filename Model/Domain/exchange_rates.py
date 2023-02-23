from Utils.utils import Base
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey, Double


class ExchangeRates(Base):
    __tablename__ = "exchange_rates"
    id = Column(Integer, primary_key=True)
    from_currency = Column(String(3))
    to_currency = Column(String(3))
    date_time = Column(DateTime)
    rate = Column(Float(2))
    def __repr__(self):
        return f'{self.id}; {self.from_currency}; {self.to_currency}; {self.date_time}; {self.rate}'

    def __str__(self):
        return f'{self.id}; {self.from_currency}; {self.to_currency}; {self.date_time}; {self.rate}'