class UserCredentials:
    def __init__(self, user_id, username, user_password_hash):
        """

        :param user_id: acelasi id folosit si in User class (CNP)
        :param username: username, unique
        :param user_password_hash:
        """
        self.__user_id = user_id
        self.__username = username
        self.__user_password_hash = user_password_hash

    def __str__(self):
        return f'{self.__user_id};{self.__username};{self.__user_password_hash}'

    def __repr__(self):
        return f'{self.__user_id};{self.__username};{self.__user_password_hash}'

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_username(self):
        return self.__username

    def set_username(self, usernamechosen):
        self.__username = usernamechosen




