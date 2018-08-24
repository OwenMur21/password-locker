import unittest 
from user import User , Credentials

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

    
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Test","34huhuhuhu") # new user
        test_user.save_user()

        user_exists = User.user_exist("Test")

        self.assertTrue(user_exists)


class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_credentials = Credentials ("Reddit","ozzyman","23iiihihs") #create user object

    def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """ 
        Credentials.credentials_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.acc_name,"Reddit")

    def test_save_credentials(self):
        """
        test to check if the credentials object is saved on credentials list
        """
        self.new_credentials.save_credentials() #save user
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        """
        To check if we can save multiple objects into list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Twitter","khaleesifan","24hugugugu")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
            '''
            test_delete_contact to test if we can remove credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials ("Twitter","khaleesifan","24hugugugu") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credentials object
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_acc_name(self):
        '''
        test to check if we can find a credential by account name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Twitter","khaleesifan","24hugugugu") # new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_acc_name("Twitter")

        self.assertEqual(found_credentials.pword,test_credentials.pword)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Twitter","khaleesifan","24hugugugu") # new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Twitter")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentialss saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()