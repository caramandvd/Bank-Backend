class UsersDeposits:
    def __init__(self, user_id, currency, name, amount, description):
        self.__user_id = user_id
        self.__currency = currency
        self.__name = name
        self.__amount = amount
        self.__description = description

    def __str__(self):
        return f'{self.__user_id};{self.__currency};{self.__name};{self.__amount};{self.__description}'

    def __repr__(self):
        return f'{self.__user_id};{self.__currency};{self.__name};{self.__amount};{self.__description}'

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description