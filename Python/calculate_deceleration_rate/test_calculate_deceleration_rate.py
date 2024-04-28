import unittest

def calc_deceleration_rate(initial_velocity, final_velocity, time):
    if time == 0:
        raise ValueError("Time cannot be zero.")
    if not (isinstance(initial_velocity, (int, float)) and isinstance(final_velocity, (int, float)) and isinstance(time, (int, float))):
        raise ValueError("All parameters must be numeric.")
    if initial_velocity <= final_velocity:
        raise ValueError("Initial velocity must be greater than final velocity for deceleration.")
    if time < 0:
        raise ValueError("Time must be positive.")

    deceleration_rate = (initial_velocity - final_velocity) / time
    return deceleration_rate

class TestCalcDecelerationRate(unittest.TestCase):
    def test_correct_calculation(self):
        result = calc_deceleration_rate(100, 50, 10)
        self.assertEqual(result, 5)

    def test_zero_time(self):
        with self.assertRaises(ValueError) as context:
            calc_deceleration_rate(100, 50, 0)
        self.assertTrue("Time cannot be zero." in str(context.exception))

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError) as context:
            calc_deceleration_rate('100', 50, 10)
        self.assertTrue("All parameters must be numeric." in str(context.exception))

    def test_negative_time(self):
        with self.assertRaises(ValueError) as context:
            calc_deceleration_rate(100, 50, -10)
        self.assertTrue("Time must be positive." in str(context.exception))

    def test_invalid_velocity_values(self):
        with self.assertRaises(ValueError) as context:
            calc_deceleration_rate(50, 100, 10)
        self.assertTrue("Initial velocity must be greater than final velocity for deceleration." in str(context.exception))

if __name__ == '__main__':
    unittest.main()
