import unittest
from calculate_final_velocity import calc_final_velocity

class TestCalcFinalVelocity(unittest.TestCase):

    def test_basic_deceleration(self):
        result = calc_final_velocity(100, 10, 5)
        self.assertEqual(result, 50)

    def test_zero_time(self):
        result = calc_final_velocity(50, 20, 0)
        self.assertEqual(result, 50)

    def test_zero_deceleration(self):
        result = calc_final_velocity(30, 0, 10)
        self.assertEqual(result, 30)

    def test_negative_initial_velocity(self):
        result = calc_final_velocity(-10, 5, 2)
        self.assertEqual(result, -20)

    def test_negative_time_error(self):
        with self.assertRaises(ValueError):
            calc_final_velocity(100, 10, -1)

    def test_invalid_input_types(self):
        with self.assertRaises(ValueError):
            calc_final_velocity("100", 10, 5)
        with self.assertRaises(ValueError):
            calc_final_velocity(100, "10", 5)
        with self.assertRaises(ValueError):
            calc_final_velocity(100, 10, "5")

if __name__ == "__main__":
    unittest.main()
