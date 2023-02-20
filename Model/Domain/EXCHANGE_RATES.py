class ExchangeRates:
    def __init__(self, id, from_currency, to_currency, date_time, rate):
        self.__id = id
        self.__from_currency = from_currency
        self.__to_currency = to_currency
        self.__date_time = date_time
        self.__rate = rate

    def __repr__(self):
        return f'{self.__id};{self.__from_currency};{self.__to_currency};{self.__date_time};{self.__rate}'

    def __str__(self):
        return f'{self.__id};{self.__from_currency};{self.__to_currency};{self.__date_time};{self.__rate}'

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_from_currency(self):
        return self.__from_currency

    def set_from_currency(self, from_currency):
        self.__from_currency = from_currency

    def get_to_currency(self):
        return self.__to_currency

    def set_to_currency(self, to_currency):
        self.__to_currency = to_currency

    def get_date_time(self):
        return self.__date_time

    def set_date_time(self, date_time):
        self.__date_time = date_time

    def get_rate(self):
        return self.__rate

    def set_rate(self, rate):
        self.__rate = rate