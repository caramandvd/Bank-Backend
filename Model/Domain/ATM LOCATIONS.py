class AtmLocations:
    def __init__(self, atm_id, address, lat, lng, number_atms):
        self.__atm_id = atm_id
        self.__address = address
        self.__lat = lat
        self.__lng = lng
        self.__number_atms = number_atms

    def get_atm_id(self):
        return self.__atm_id

    def set_atm_id(self, id_atm):
        self.__atm_id = id_atm

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_lat(self):
        return self.__lat

    def set_lat(self, lat):
        self.__lat = lat

