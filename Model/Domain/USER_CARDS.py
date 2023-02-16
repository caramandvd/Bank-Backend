class UserCards:
    def __init__(self, user_id, card_number, pin_hash, cvv_hash, expiration_date):
        self.__user_id = user_id
        self.__card_number = card_number
        self.__pin_hash = pin_hash
        self.__cvv_hash = cvv_hash
        self.__expiration_date = expiration_date

    def __repr__(self):
        return f'{self.__user_id};{self.__card_number};{self.__pin_hash};{self.__cvv_hash};{self.__expiration_date}'

    def __str__(self):
        return f'{self.__user_id};{self.__card_number};{self.__pin_hash};{self.__cvv_hash};{self.__expiration_date}'

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self, cardnumber):
        self.__card_number = cardnumber

    def get_pin_hash(self):
        return self.__pin_hash

    def set_pin_hash(self, pinhash):
        self.__pin_hash = pinhash

    def get_cvv_hash(self):
        return self.__cvv_hash

    def set_cvv_hash(self, cvvhash):
        self.__cvv_hash = cvvhash

    def get_expiration_date(self):
        return self.__expiration_date

    def set_expiration_date(self, expdate):
        self.__expiration_date = expdate
