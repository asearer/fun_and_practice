# test_auth.py
import unittest
from auth import login

class TestLoginFunction(unittest.TestCase):
    def test_correct_credentials(self):
        """ Test that the correct credentials return True """
        self.assertTrue(login("admin", "admin"))

    def test_incorrect_username(self):
        """ Test that an incorrect username returns False """
        self.assertFalse(login("user", "admin"))

    def test_incorrect_password(self):
        """ Test that an incorrect password returns False """
        self.assertFalse(login("admin", "password"))

    def test_incorrect_both(self):
        """ Test that incorrect username and password return False """
        self.assertFalse(login("user", "password"))

    def test_empty_username(self):
        """ Test that an empty username returns False """
        self.assertFalse(login("", "admin"))

    def test_empty_password(self):
        """ Test that an empty password returns False """
        self.assertFalse(login("admin", ""))

    def test_empty_both(self):
        """ Test that empty username and password return False """
        self.assertFalse(login("", ""))

    def test_none_username(self):
        """ Test that None as username returns False """
        self.assertFalse(login(None, "admin"))

    def test_none_password(self):
        """ Test that None as password returns False """
        self.assertFalse(login("admin", None))

    def test_none_both(self):
        """ Test that None username and password return False """
        self.assertFalse(login(None, None))

if __name__ == '__main__':
    unittest.main()
