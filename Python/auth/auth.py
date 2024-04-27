def login(username, password):
    """
    Check if the given username and password match the expected "admin" credentials.
    
    Parameters:
    username (str): The username to check.
    password (str): The password to check.
    
    Returns:
    bool: True if both username and password are "admin", False otherwise.
    """
    return username == "admin" and password == "admin"
