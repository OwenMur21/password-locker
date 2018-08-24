import string
from random import choice

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

class Credentials:
    """
    Class that generates new instances of credentials
    """

    credentials_list = [] #Empty credential 

    def __init__(self,acc_name,login_name,pword):
        """
        __init__ method that defines properties for our objects

        Args:
            acc_name: New credentials acc_name.
            login_name: New credentials login_name.
            pword: New credentials pword.
        """

        self.acc_name = acc_name
        self.login_name = login_name
        self.pword = pword

    def save_credentials(self):
        """
        save_credentials method saves objects into list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    def gen_password(self):
        """
        gen_password method that generates random passwords
        """
        alphabet = string.ascii_letters + string.digits
        password = ''.join(choice(alphabet) for i in range(8))
    @classmethod
    def find_by_acc_name(cls,acc_name):
        '''
        Method that takes in a number and returns a credential that matches that account name.

        Args:
            acc_name: Account name to search for
        Returns :
            Credential of account that matches the account name.
        '''

        for credentials in cls.credentials_list:
            if credentials.acc_name == acc_name:
                return credentials
    @classmethod
    def credentials_exist(cls,acc_name):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            acc_name: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.acc_name == acc_name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
