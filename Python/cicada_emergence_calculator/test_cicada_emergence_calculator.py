import unittest
from cicada_emergence_calculator import calculate_next_emergence

class TestCicadaEmergence(unittest.TestCase):
    
    def test_17_year_period(self):
        self.assertEqual(calculate_next_emergence(2004, 17), 2021, "Should be 2021 for 17-year period from 2004")
        self.assertEqual(calculate_next_emergence(1987, 17), 2004, "Should be 2004 for 17-year period from 1987")
    
    def test_13_year_period(self):
        self.assertEqual(calculate_next_emergence(2004, 13), 2017, "Should be 2017 for 13-year period from 2004")
        self.assertEqual(calculate_next_emergence(1991, 13), 2004, "Should be 2004 for 13-year period from 1991")
    
    def test_edge_cases(self):
        self.assertEqual(calculate_next_emergence(0, 17), 17, "Should be 17 for 17-year period from year 0")
        self.assertEqual(calculate_next_emergence(0, 13), 13, "Should be 13 for 13-year period from year 0")
        self.assertEqual(calculate_next_emergence(2024, 17), 2041, "Should be 2041 for 17-year period from 2024")
        self.assertEqual(calculate_next_emergence(2024, 13), 2037, "Should be 2037 for 13-year period from 2024")
    
    def test_invalid_period(self):
        with self.assertRaises(ValueError):
            calculate_next_emergence(2004, 15)

if __name__ == '__main__':
    unittest.main()

