import unittest
import os

def generate_salt():
    """
    Generates a random salt.

    Returns:
        str: A random salt value.
    """
    salt = os.urandom(16)
    return salt.hex()

class TestGenerateSalt(unittest.TestCase):
    def test_generate_salt(self):
        salt = generate_salt()
        self.assertEqual(len(salt), 32)  # 16 bytes represented as 32 hex characters

if __name__ == '__main__':
    unittest.main()
