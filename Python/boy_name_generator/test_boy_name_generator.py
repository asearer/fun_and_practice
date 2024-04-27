import unittest
from boy_name_generator import get_random_boy_names  

class TestBoyNamesGenerator(unittest.TestCase):

    def test_count_of_names(self):
        """Test that the function returns exactly 20 names."""
        result = get_random_boy_names()
        self.assertEqual(len(result), 20)

    def test_no_empty_names(self):
        """Test that there are no empty names in the list."""
        result = get_random_boy_names()
        self.assertTrue(all(name != '' for name in result))

    def test_all_names_from_list(self):
        """Test that all returned names are in the predefined list of names."""
        boys = ["Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
                "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo"]
        result = get_random_boy_names()
        self.assertTrue(all(name in boys for name in result))

if __name__ == '__main__':
    unittest.main()
