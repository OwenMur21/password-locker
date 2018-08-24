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

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.acc_name,"Reddit")



if __name__ == '__main__':
    unittest.main()