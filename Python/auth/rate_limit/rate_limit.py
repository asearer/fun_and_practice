import time

class RateLimiter:
    def __init__(self, limit, interval):
        """
        Initializes the RateLimiter with a request limit and interval.

        Args:
            limit (int): The maximum number of requests allowed within the interval.
            interval (float): The time interval (in seconds) for rate limiting.
        """
        self.limit = limit
        self.interval = interval
        self.requests = []

    def allow_request(self):
        """
        Checks if a request is allowed based on the rate limit.

        Returns:
            bool: True if the request is allowed, False otherwise.
        """
        current_time = time.time()
        # Remove requests that are older than the interval
        self.requests = [req for req in self.requests if req >= current_time - self.interval]
        # If the number of requests is less than the limit, allow the request
        if len(self.requests) < self.limit:
            self.requests.append(current_time)
            return True
        else:
            return False

# Example usage
limiter = RateLimiter(limit=5, interval=60)  # Allow 5 requests per minute
for i in range(7):
    if limiter.allow_request():
        print("Request", i+1, "allowed.")
    else:
        print("Request", i+1, "blocked due to rate limiting.")
