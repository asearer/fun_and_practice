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
    # Combine password and salt, then hash using SHA-256
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

# Example usage
password = input("Enter your password: ")
salt = "random_salt_here"  # Generate a unique salt for each user
hashed_password = hash_password(password, salt)
print("Hashed password:", hashed_password)
