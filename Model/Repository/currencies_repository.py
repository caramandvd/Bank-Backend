from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from Model.Domain.currencies import Currencies
from Utils.utils import Base


class CurrenciesRepository:
    def __init__(self):
        self.session = sessionmaker(create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb'))()

    def read(self):
        return self.session.query(Currencies).all()

    def create(self, currency):
        new_currency = Currencies(
            currency=currency
        )
        self.session.add(new_currency)
        self.session.commit()


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')
    Base.metadata.create_all(engine)
    repo = CurrenciesRepository()
    repo.create('DKK')
    print(repo.read())