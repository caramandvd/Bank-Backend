from datetime import datetime

from sqlalchemy.orm import sessionmaker

from model.domain.exchange_rates import ExchangeRates
from utils.db import Base, engine


class ExchangeRatesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def read(self, exchange_id):
        return self.session.query(ExchangeRates).filter_by(exchange_id=exchange_id).first()

    def create(self, from_currency, to_currency, rate):
        new_exchange_rate = ExchangeRates(
            from_currency=from_currency,
            to_currency=to_currency,
            rate=rate,
            date_time=datetime.now()
        )
        self.session.add(new_exchange_rate)
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = ExchangeRatesRepository()
    repo.create('RON', 'EUR', 0.201)
    print(repo.read(3))
