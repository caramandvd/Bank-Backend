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
        return f'{self.__id};{self.__user_id};{self.__message};{self.__date};{self.__state}'

    def __repr__(self):
        return f'{self.__id};{self.__user_id};{self.__message};{self.__date};{self.__state}'

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id
        
    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_message(self):
        return self.__message

    def set_message(self, message):
        self.__message = message

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state