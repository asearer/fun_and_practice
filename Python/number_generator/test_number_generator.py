import unittest
import random

def generate_numbers():
    return [random.randint(1, 5000) for _ in range(5000)]

class TestRandomNumbers(unittest.TestCase):
    def setUp(self):
        self.numbers = generate_numbers()

    def test_length_of_list(self):
        self.assertEqual(len(self.numbers), 5000, "The list should contain 5000 elements.")

    def test_range_of_values(self):
        for num in self.numbers:
            self.assertTrue(1 <= num <= 5000, f"Each number must be between 1 and 5000, found {num}.")

    def test_type_of_elements(self):
        for num in self.numbers:
            self.assertIsInstance(num, int, f"Each number should be an integer, found type {type(num)}.")

if __name__ == "__main__":
    unittest.main()
