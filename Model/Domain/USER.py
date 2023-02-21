import datetime

class User:
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

    def __str__(self):
        return f'{self.__user_id};{self.__first_name};{self.__last_name};{self.__email_name};{self.__address};' \
               f'{self.__phone_number};{self.__date_of_birth};{self.__join_date}\n'

    def __repr__(self):
        return f'{self.__user_id};{self.__first_name};{self.__last_name};{self.__email_name};{self.__address};' \
               f'{self.__phone_number};{self.__date_of_birth};{self.__join_date}\n'

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, firstname):
        self.__first_name = firstname

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, lastname):
        self.__last_name = lastname

    def get_user_id(self):
        return self.__user_id

    def get_email_name(self):
        return self.__email_name

    def set_email_name(self, emailname):
        self.__email_name = emailname

    def get_adress(self):
        return self.__address

    def set_adress(self, adress):
        self.__address = adress

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phonenumber):
        self.__phone_number = phonenumber

    def get_birth_of_date(self):
        """Split the date parts from the number and return the birth date."""
        centuries = {
            '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
        }  # we assume 1900 for the others in order to try to construct a date
        year = int(self.__user_id[1:3]) + centuries.get(self.__user_id[0], 1900)
        month = int(self.__user_id[3:5])
        day = int(self.__user_id[5:7])
        try:
            return datetime.date(year, month, day)
        except ValueError:
            from stdnum.exceptions import InvalidComponent
            raise InvalidComponent()
