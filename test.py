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

if __name__ == '__main__':
    unittest.main()