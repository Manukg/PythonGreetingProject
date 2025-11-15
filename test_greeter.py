import unittest
from greeter import greet

class TestGreet(unittest.TestCase):

    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Welcome, Alice!!")

    def test_greet_without_name(self):
        self.assertEqual(greet(), "Welcome!")

if __name__ == "__main__":
    unittest.main()
