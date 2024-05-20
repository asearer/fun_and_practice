import unittest
import secrets

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        session_token = secrets.token_hex(16)
        self.sessions[session_token] = user_id
        return session_token

    def validate_session(self, session_token):
        return self.sessions.get(session_token)

class TestSessionManager(unittest.TestCase):
    def setUp(self):
        self.manager = SessionManager()

    def test_create_session(self):
        user_id = "12345"
        session_token = self.manager.create_session(user_id)
        self.assertEqual(len(session_token), 32)
        self.assertEqual(self.manager.validate_session(session_token), user_id)

    def test_validate_session(self):
        user_id = "12345"
        session_token = self.manager.create_session(user_id)
        self.assertEqual(self.manager.validate_session(session_token), user_id)
        self.assertIsNone(self.manager.validate_session("invalid_token"))

if __name__ == '__main__':
    unittest.main()
