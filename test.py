import unittest 
import pyperclip
from user import User , Credential

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_user = User ("Ozzie","21ozwellyeah") #create user object


    def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """ 
        User.user_list = []
        

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username,"Ozzie")

    def test_save_user(self):
        """
        test to check if the user object is saved on user list
        """
        self.new_user.save_user() #save user
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_user(self):
        """
        To check if we can save multiple objects into list
        """
        self.new_user.save_user()
        test_user = User ("Test","34huhuhuhu")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User ("khaleesifna","24hugugugu") # new user
        test_user.save_user()

        found_user = User.find_by_username("khaleesifna")

        self.assertEqual(found_user.password,test_user.password)

    
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Test","34huhuhuhu") # new user
        test_user.save_user()

        user_exists = User.user_exist("Test")

        self.assertTrue(user_exists)


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_credential = Credential ("Reddit","ozzyman","23iiihihs") #create user object

    def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """ 
        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.acc_name,"Reddit")

    def test_save_credential(self):
        """
        test to check if the credential object is saved on credential list
        """
        self.new_credential.save_credential() #save user
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        """
        To check if we can save multiple objects into list
        """
        self.new_credential.save_credential()
        test_credential = Credential ("Twitter","khaleesifan","24hugugugu")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
            '''
            test_delete_contact to test if we can remove credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential ("Twitter","khaleesifan","24hugugugu") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_acc_name(self):
        '''
        test to check if we can find a credential by account name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential ("Twitter","khaleesifan","24hugugugu") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_acc_name("Twitter")

        self.assertEqual(found_credential.pword,test_credential.pword)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential ("Twitter","khaleesifan","24hugugugu") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Twitter")

        self.assertTrue(credential_exists)

    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credential_list)

    # def test_copy_login_name(self):
    #     '''
    #     Test to confirm that we are copying the login name from a found credential
    #     '''

    #     self.new_credential.save_credential()
    #     credential.copy_login_name("Twitter")
    #     self.assertEqual(self.new_credential.login_name,pyperclip.paste())

    


if __name__ == '__main__':
    unittest.main()