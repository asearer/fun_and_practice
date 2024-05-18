import secrets

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        """
        Creates a new session for the given user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The generated session token.
        """
        session_token = secrets.token_hex(16)
        self.sessions[session_token] = user_id
        return session_token

    def validate_session(self, session_token):
        """
        Validates the provided session token.

        Args:
            session_token (str): The session token to validate.

        Returns:
            str: The ID of the user associated with the session token, or None if invalid.
        """
        return self.sessions.get(session_token)

# Example usage
session_manager = SessionManager()
user_id = "12345"
session_token = session_manager.create_session(user_id)
print("Session token:", session_token)
print("Validating session:", session_manager.validate_session(session_token))
