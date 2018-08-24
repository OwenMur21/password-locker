#!/usr/bin/env python3.6
import string
from random import choice
from user import User , Credentials
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User (username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def check_existing_users(surname):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(surname)

def create_credentials(acc_name,login_name,pword):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials (acc_name,login_name,pword)
    return new_credentials

def save_credentialss(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()

def generate_password(self):
    """
    Function to generate random password
    """
    return password

def find_credentials(acc_name):
    '''
    Function that finds a credential by acc_name and returns the credential
    '''
    return Credentials.find_by_acc_name(acc_name)

def check_existing_contacts(number):
    '''
    Function that check if a credential exists with that acc_name and return a Boolean
    '''
    return Credentials.credentials_exist(number)

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()

# def copy_credentials_login_name(acc_name):
#     '''
#     Function that copies login name to clipboard
#     '''
#     return Credentials.copy_login_name(acc_name)


def main():
    print("WELCOME TO PASSWORD LOCKER. ")
print('\n')



if __name__ == '__main__':
    main()










