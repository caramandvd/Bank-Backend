from sqlalchemy import Column, String, ForeignKey

from utils.db import Base


class UsersCredentials(Base):
    __tablename__ = "users_credentials"

    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey("users.user_id", ondelete="CASCADE"))
    username = Column(String(30), unique=True)
    user_password_hash = Column(String(25))

    def __str__(self):
        return f'{self.user_id}; {self.username}; {self.user_password_hash}'

    def __repr__(self):
        return f'{self.user_id}; {self.username}; {self.user_password_hash}'
