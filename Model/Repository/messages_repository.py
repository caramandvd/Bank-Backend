from datetime import datetime
from sqlalchemy.orm import sessionmaker
from Model.Domain.messages import Messages
from Utils.utils import Base, engine


class MessagesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def read(self, id):
        return self.session.query(Messages).filter_by(id=id).first()

    def update(self, id, **kwargs):
        self.session.query(Messages).filter_by(id=id).update(kwargs)
        self.session.commit()

    def create(self, user_id, message, state):
        new_message = Messages(
            user_id=user_id,
            message=message,
            date=datetime.now(),
            state=state
        )
        self.session.add(new_message)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = MessagesRepository()
    repo.create('5030329082416', 'This is the first sent message', True)
    print(repo.read(1))
