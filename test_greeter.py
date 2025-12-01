'''
Unit Test For the module
'''
import unittest
from greeter import greet
class TestGreet(unittest.TestCase):
    '''
    Test Class
    '''
    def test_greet_with_name(self):
        '''Testing Return Value'''
        self.assertEqual(greet("Alice"), "Welcome, Alice!")
    def test_greet_without_name(self):
        '''Testing the Null Value'''
        self.assertEqual(greet(), "Welcome!")

if __name__ == "__main__":
    unittest.main()
