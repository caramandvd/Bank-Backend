from sqlalchemy.orm import sessionmaker
from Model.Domain.currencies import Currencies
from Utils.utils import Base, engine


class CurrenciesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def read(self):
        return self.session.query(Currencies).all()

    def create(self, currency):
        new_currency = Currencies(
            currency=currency
        )
        self.session.add(new_currency)
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = CurrenciesRepository()
    repo.create('DKK')
    print(repo.read())
