import unittest

def find_largest_word(input_string):
    words = input_string.split()
    return max(words, key=len) if words else ""

class TestFindLargestWord(unittest.TestCase):
    def test_regular_sentence(self):
        self.assertEqual(find_largest_word("Hello there world"), "Hello")

    def test_longest_word_repeated(self):
        self.assertEqual(find_largest_word("wow amazing amazing wow"), "amazing")

    def test_same_length_words(self):
        self.assertEqual(find_largest_word("cat bat mat"), "cat")

    def test_empty_string(self):
        self.assertEqual(find_largest_word(""), "")

    def test_with_punctuation(self):
        # This test assumes that punctuation is considered part of the word
        self.assertEqual(find_largest_word("hello, world!"), "hello,")

    def test_single_word(self):
        self.assertEqual(find_largest_word("loneliness"), "loneliness")

    def test_various_whitespace(self):
        self.assertEqual(find_largest_word("  data \tscience\r\nis awesome  "), "science")

# Running the tests
if __name__ == "__main__":
    unittest.main()
