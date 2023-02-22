from Utils.utils import Base
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey


class UsersCredentials(Base):
    __tablename__ = "users_credentials"

    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey("users.user_id", ondelete="CASCADE"))
    username = Column(String(30), unique=True)
    user_password_hash = Column(String(25))

    def __str__(self):
        return f'{self.__user_id};{self.__username};{self.__user_password_hash}'

    def __repr__(self):
        return f'{self.__user_id};{self.__username};{self.__user_password_hash}'

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_username(self):
        return self.__username

    def set_username(self, usernamechosen):
        self.__username = usernamechosen




