from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, Double, Boolean


class Messages(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey('users.user_id', ondelete="CASCADE"))
    messages = Column(String)
    date = Column(Date)
    state = Column(Boolean)

    def __str__(self):
        return f'{self.id};{self.user_id};{self.message};{self.date};{self.state}'

    def __repr__(self):
        return f'{self.id};{self.user_id};{self.message};{self.date};{self.state}'