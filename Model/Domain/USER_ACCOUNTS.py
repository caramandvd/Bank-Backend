class UserAccounts:
    def __init__(self, user_id, account_number, currency, amount):
        self.__user_id = user_id
        self.__account_number = account_number
        self.__currency = currency
        self.__amount = amount

    def __repr__(self):
        return f'{self.__user_id};{self.__account_number};{self.__currency};{self.__amount}'

    def __str__(self):
        return f'{self.__user_id};{self.__account_number};{self.__currency};{self.__amount}'

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id