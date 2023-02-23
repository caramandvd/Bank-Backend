from Utils.utils import Base
from sqlalchemy import Column, String, Integer


class AtmLocations(Base):
    __tablename__ = "atm_locations"
    atm_id = Column(String(9), primary_key=True)
    address = Column(String(200))
    lat = Column(String(9))
    lng = Column(String(9))
    number_atms = Column(Integer, auto_increment=True)

    def __repr__(self):
        return f'{self.atm_id}; {self.address}; {self.lat}; {self.lng}; {self.number_atms}'