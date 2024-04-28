import unittest
from calculate_acceleration_rate import calc_acceleration_rate  # Import the function from your module.

class TestCalcAccelerationRate(unittest.TestCase):
    def test_normal_conditions(self):
        # Test under normal conditions.
        self.assertAlmostEqual(calc_acceleration_rate(0, 10, 2), 5.0)
        self.assertAlmostEqual(calc_acceleration_rate(10, 20, 5), 2.0)

    def test_negative_time(self):
        # Test with negative time to ensure it handles as expected.
        self.assertAlmostEqual(calc_acceleration_rate(0, 10, -2), -5.0)
        self.assertAlmostEqual(calc_acceleration_rate(10, 20, -5), -2.0)

    def test_zero_time(self):
        # Test with zero time to check for proper exception handling.
        with self.assertRaises(ValueError):
            calc_acceleration_rate(0, 10, 0)

    def test_negative_acceleration(self):
        # Test for negative acceleration (slowing down).
        self.assertAlmostEqual(calc_acceleration_rate(20, 10, 5), -2.0)

    def test_deceleration_negative_time(self):
        # Test for deceleration with negative time.
        self.assertAlmostEqual(calc_acceleration_rate(20, 10, -5), 2.0)

if __name__ == '__main__':
    unittest.main()
