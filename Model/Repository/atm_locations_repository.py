from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.Domain.atm_locations import AtmLocations
from Utils.utils import Base


class AtmLocationsRepository:

    def __init__(self):
        self.session = sessionmaker(create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb'))()

    def read(self, atm_id):
        return self.session.query(AtmLocations).filter_by(atm_id=atm_id).first()

    def create(self, atm_id, address, lat, lng):
        new_atm = AtmLocations(
            atm_id=atm_id,
            address=address,
            lat=lat,
            lng=lng
        )
        self.session.add(new_atm)
        self.session.commit()


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root@localhost:3306/bankdashboarddb')
    Base.metadata.create_all(engine)
    repo = AtmLocationsRepository()
    repo.create('000000001', 'Sigma, Zorilor', '46 45 24.1N', '23 35 40.9E')
    print(repo.read('000000001'))