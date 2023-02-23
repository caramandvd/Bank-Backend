from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')
    Base.metadata.create_all(engine)
    repo = UsersTransactionsRepository()