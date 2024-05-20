import unittest
import time

def perform_task():
    start_time = time.time()
    time.sleep(0.02)  # Simulating a time-consuming task
    return time.time() - start_time

class TestPerformance(unittest.TestCase):
    def test_performance(self):
        execution_time = perform_task()
        self.assertLess(execution_time, 0.03)  # Check if the task finishes within the expected time frame

if __name__ == '__main__':
    unittest.main()
