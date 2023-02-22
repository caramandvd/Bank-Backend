from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, Double


class AtmLocations(Base):
    __tablename__ = "atm_locations"
    atm_id = Column(String(9), primary_key=True)
    address = Column(String(200))
    lat = Column(String(9))
    lng = Column(String(9))
    number_atms = Column(Integer)
