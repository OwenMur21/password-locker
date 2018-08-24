import unittest 
from user import User

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

if __name__ == '__main__':
    unittest.main()