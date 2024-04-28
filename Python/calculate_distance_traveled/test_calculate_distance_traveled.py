import unittest

# Assuming calc_distance_traveled is defined in a module named distance_calculator
from calculate_distance_traveled import calc_distance_traveled

class TestCalcDistanceTraveled(unittest.TestCase):
    def test_typical_case(self):
        """Test that the function computes the correct distance with typical values."""
        self.assertAlmostEqual(calc_distance_traveled(10, 20, 5), 75.0)

    def test_zero_time(self):
        """Test that the function returns zero when time is zero."""
        self.assertEqual(calc_distance_traveled(10, 20, 0), 0)

    def test_negative_time(self):
        """Test that the function raises ValueError when time is negative."""
        with self.assertRaises(ValueError):
            calc_distance_traveled(10, 20, -5)

    def test_zero_initial_and_final_velocity(self):
        """Test that the function returns zero when both velocities are zero."""
        self.assertEqual(calc_distance_traveled(0, 0, 10), 0)

    def test_type_error_with_string(self):
        """Test that the function raises TypeError when inputs are not numbers."""
        with self.assertRaises(TypeError):
            calc_distance_traveled("10", "20", "5")

    def test_with_float_values(self):
        """Test the function with floating-point values."""
        self.assertAlmostEqual(calc_distance_traveled(5.5, 10.5, 2.0), 16.0)

# This allows the test suite to be run from the command line
if __name__ == '__main__':
    unittest.main()
