import random
import string

class User:
    """
    Class that generates new instances of users.
    """
    user_list = []
    def __init__(self,username,password):

        self.username = username
        self.password = password
   
    def save_user(self):
        '''
        this method add users to the user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        this method removes users form the user_list
        '''
        User.user_list.remove(self)
    @classmethod
    def user_exists(cls,username,password):
        '''
        this method checks if a specified user exists in the application
        '''
        current_user = ""
        for user in cls.user_list:
            if user.username == username and user.password == password:
                current_user = user.username
                return current_user


class Credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list = []
    def __init__(self,account,username,password):

        self.account = account
        self.username = username
        self.password = password
       
    def save_credentials(self):
        '''
        this method will add credentials to the credentials_list
        '''
        Credentials.credentials_list.append
    def delete_credentials(self):
        '''
        this method will remove credentials form the credentials_list
        '''
        Credentials.credentials_list.remove

  
    def get_random_password(stringLength = 8):
        '''
        this method randomly generates passwords for the users
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits 
        return ''.join(random.choice(password) for i in range(stringLength))


    @classmethod
    def display_credentials(cls):
        '''
        this method displays all the credentials save in the account
        '''
        return cls.credentials_list

    @classmethod
    def find_account(cls,account):
        '''
        this method searches for a specific account as specified by the user
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials