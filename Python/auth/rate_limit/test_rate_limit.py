import unittest
import time

class RateLimiter:
    def __init__(self, limit, interval):
        self.limit = limit
        self.interval = interval
        self.requests = []

    def allow_request(self):
        current_time = time.time()
        self.requests = [req for req in self.requests if req >= current_time - self.interval]
        if len(self.requests) < self.limit:
            self.requests.append(current_time)
            return True
        else:
            return False

class TestRateLimiter(unittest.TestCase):
    def test_allow_request(self):
        limiter = RateLimiter(limit=3, interval=1)
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertTrue(limiter.allow_request())
        self.assertFalse(limiter.allow_request())
        time.sleep(1.1)
        self.assertTrue(limiter.allow_request())

if __name__ == '__main__':
    unittest.main()
