"""
TO DO:
Create
Read
Update
Delete
Get All
Get email by user_id
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing import db

Base = declarative_base()


class UserRepository(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    join_date = Column(DateTime, nullable=True)

    def __init__(self, user_id, first_name, last_name, email_name, address, phone_number, date_of_birth, join_date):
        """

        :param user_id: CNP-ul clientului, -int, 13 caractere
        :param first_name: numele clientului, -str
        :param last_name: prenumele clientului, -str
        :param email_name: email client,
        :param address: adresa clientului, -str
        :param phone_number: numarul de telefon al clientului, -str
        :param date_of_birth: data nasterii, date
        :param join_date: data in care a devenit client/ adaugarea clientului, date
        """
        self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_name = email_name
        self.__address = address
        self.__phone_number = phone_number
        self.__date_of_birth = date_of_birth
        self.__join_date = join_date

    def __repr__(self):
        return f'{self.user_id}; {self.first_name}; {self.last_name}; {self.email_name}; {self.address}; ' \
               f'{self.phone_number}; {self.date_of_birth}; {self.join_date}\n'

    #getting all users
    # def create_user(self)

    def read_users(self):
        engine = create_engine('mysql+pymysql://root:@localhost:3306/bankdashboarddb', echo=True)
        Session = sessionmaker(bind=engine)
        my_session = Session()

        all_users = my_session.query(UserRepository).all()
        print(all_users)

    def read_single_user(self, searched_id):
        engine = create_engine('mysql+pymysql://root:@localhost:3306/bankdashboarddb', echo=True)
        Session = sessionmaker(bind=engine)
        my_session = Session()
        user = my_session.query(UserRepository).get(searched_id)
        print(user)

    # def update_user(self, new_user_id, new_first_name, new_last_name, new_email_name, new_address, new_phone_number, new_date_of_birth, new_join_date):
if __name__ == "__main__":
        engine = create_engine('mysql+pymysql://root:@localhost:3306/bankdashboarddb', echo=True)
        Session = sessionmaker(bind=engine)
        my_session = Session()

        user_id = input("user id:")
        first_name = input("First Name:")
        last_name = input("Last Name:")
        email_name = input("E-mail:")
        address = input("Address:")
        phone_number = input("Phone Number:")
        date_of_birth = input("Date of Birth:")
        join_date = "2023-02-21"

        new_user = UserRepository(user_id, first_name, last_name, email_name, address, phone_number, date_of_birth, join_date)
        db.session.add(new_user)
        db.session.commit()

        return users.add(new_user)