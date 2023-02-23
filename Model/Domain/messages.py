from Utils.utils import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime


class Messages(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(13), foreign_key=ForeignKey('users.user_id', ondelete="CASCADE"))
    message = Column(String)
    date = Column(DateTime)
    state = Column(Boolean)

    def __str__(self):
        return f'{self.id}; {self.user_id}; {self.message}; {self.date}; {self.state}'

    def __repr__(self):
        return f'{self.id}; {self.user_id}; {self.message}; {self.date}; {self.state}'