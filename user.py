class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] #Empty user list

    def __init__(self,username,password):
        """
        __init__ method that defines properties for our objects

        Args:
            username: New user username.
            password: New user password.
        """

        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves objects into list
        """
        User.user_list.append(self)


    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False    
