import unittest
import hashlib

def hash_password(password, salt):
    """
    Hashes the provided password using SHA-256 algorithm with a salt.

    Args:
        password (str): The password to hash.
        salt (str): A unique salt value.

    Returns:
        str: The hashed password.
    """
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

class TestHashPassword(unittest.TestCase):
    def test_hash_password(self):
        password = "mysecretpassword"
        salt = "randomsalt"
        expected_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        self.assertEqual(hash_password(password, salt), expected_hash)

if __name__ == '__main__':
    unittest.main()
