from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    try:
        engine.connect()
        print("Success")
    except SQLAlchemyError as err:
        print("Error", err.__cause__)
