import unittest
from filter_content import filter_content

class TestFilterContent(unittest.TestCase):
    def test_valid_input(self):
        # Test with a normal string including stopwords
        self.assertEqual(filter_content("This is an example"), "example")

    def test_input_with_punctuation(self):
        # Test input string with punctuation to see if they're correctly removed
        self.assertEqual(filter_content("Hello, world! This, is a test."), "hello world test")

    def test_input_with_numbers(self):
        # Test input string with numbers to ensure they're excluded
        self.assertEqual(filter_content("This is a 1234 test"), "test")

    def test_empty_string(self):
        # Test the empty string case
        self.assertEqual(filter_content(""), "")

    def test_non_string_input(self):
        # Test with non-string input to ensure it raises a ValueError
        with self.assertRaises(ValueError):
            filter_content(123)

    def test_case_sensitivity(self):
        # Ensure that function is not case sensitive
        self.assertEqual(filter_content("ThIs Is A TEST"), "test")

if __name__ == '__main__':
    unittest.main()
