from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, Double


class AtmLocations(Base):
    __tablename__ = "atm_locations"
    atm_id = Column(String(9), primary_key=True)
    address = Column(String(200))
    lat = Column(String(9))
    lng = Column(String(9))
    number_atms = Column(Integer)
    def get_atm_id(self):
        return self.__atm_id

    def set_atm_id(self, id_atm):
        self.__atm_id = id_atm

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_lat(self):
        return self.__lat

    def set_lat(self, lat):
        self.__lat = lat

