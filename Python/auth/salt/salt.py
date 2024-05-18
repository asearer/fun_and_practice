import os
import hashlib

def generate_salt():
    """
    Generates a random salt.

    Returns:
        str: A random salt value.
    """
    # Generate a random 16-byte salt
    salt = os.urandom(16)
    return salt.hex()

# Example usage
salt = generate_salt()
print("Generated salt:", salt)
