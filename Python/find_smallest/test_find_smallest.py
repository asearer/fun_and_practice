import unittest

def find_smallest(numbers):
    """
    Finds and returns the smallest number in a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    int/float: The smallest number in the list, or None if the list is empty.
    """
    if not numbers:  # Check if the list is empty
        return None  # Return None if the list is empty to handle gracefully
    return min(numbers)

class TestFindSmallest(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(find_smallest([4, 2, 7, 1, 5]), 1)
        self.assertEqual(find_smallest([10, 20, 30, 40, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_smallest([-1, -3, -2, -5]), -5)
        self.assertEqual(find_smallest([-50, -20, -90, -10, -70]), -90)

    def test_mixed_numbers(self):
        self.assertEqual(find_smallest([1.5, -2.2, 0, 3.1]), -2.2)
        self.assertEqual(find_smallest([-100, 200, 300, -400, 500]), -400)

    def test_single_element_list(self):
        self.assertEqual(find_smallest([100]), 100)
        self.assertEqual(find_smallest([-100]), -100)

    def test_empty_list(self):
        self.assertIsNone(find_smallest([]))

if __name__ == '__main__':
    unittest.main()
