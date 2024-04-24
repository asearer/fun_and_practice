import unittest

def largest_num(nums):
    if not nums:  # Check if the list is empty
        return None  # or raise an exception, or handle it as appropriate
    largest = nums[0]  # Initialize `largest` to the first element in the list
    for num in nums:
        if num > largest:
            largest = num
    return largest

class TestLargestNum(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(largest_num([1, 2, 3, 4, 5]), 5)
        self.assertEqual(largest_num([10, 20, 30, 40, 50]), 50)

    def test_negative_numbers(self):
        self.assertEqual(largest_num([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(largest_num([-50, -20, -90, -10, -70]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(largest_num([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(largest_num([-100, 200, 300, -400, 500]), 500)

    def test_single_element_list(self):
        self.assertEqual(largest_num([100]), 100)
        self.assertEqual(largest_num([-100]), -100)

    def test_empty_list(self):
        self.assertIsNone(largest_num([]))

    def test_non_integer_types(self):
        self.assertEqual(largest_num([1.5, 2.2, 3.1]), 3.1)
        self.assertEqual(largest_num([-1.1, -2.2, -3.3]), -1.1)

    def test_list_with_duplicates(self):
        self.assertEqual(largest_num([5, 5, 5, 5, 5]), 5)
        self.assertEqual(largest_num([2, 2, 3, 3, 3, 2, 2]), 3)

    def test_list_with_all_same_elements(self):
        self.assertEqual(largest_num([7, 7, 7, 7]), 7)

if __name__ == '__main__':
    unittest.main()
