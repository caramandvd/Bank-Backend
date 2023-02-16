class Currencies:
    def __init__(self, currency):
        self.__currency = currency

    def __str__(self):
        return f'{self.__currency}'

    def __repr__(self):
        return f'{self.__currency}'

    def set_currencies(self, currency):
        self.__currency = currency

    def get_currencies(self):
        return self.__currency