from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')

try:
    engine.connect()
    print("Success")
except SQLAlchemyError as err:
    print("Error", err.__cause__)

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')
    Base.metadata.create_all(engine)
    repo = UsersTransactionsRepository()
