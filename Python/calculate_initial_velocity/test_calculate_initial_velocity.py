import unittest

# Assuming the calc_initial_velocity function is defined here
def calc_initial_velocity(final_velocity, acceleration_rate, time):
    initial_velocity = final_velocity - (acceleration_rate * time)
    return initial_velocity

class TestCalcInitialVelocity(unittest.TestCase):
    
    def test_standard_case(self):
        # Test with standard values
        result = calc_initial_velocity(100, 5, 10)
        self.assertEqual(result, 50)  # Expected: 100 - (5*10) = 50

    def test_zero_acceleration(self):
        # Test with zero acceleration, initial velocity should be equal to final velocity
        result = calc_initial_velocity(100, 0, 10)
        self.assertEqual(result, 100)

    def test_negative_acceleration(self):
        # Test with negative acceleration
        result = calc_initial_velocity(100, -5, 10)
        self.assertEqual(result, 150)  # Expected: 100 - (-5*10) = 150

    def test_zero_time(self):
        # Test with zero time, should result in final_velocity being the same as initial_velocity
        result = calc_initial_velocity(100, 5, 0)
        self.assertEqual(result, 100)

    def test_negative_time(self):
        # Test with negative time (if conceptually allowed)
        result = calc_initial_velocity(100, 5, -10)
        self.assertEqual(result, 150)  # Expected: 100 - (5*(-10)) = 150

    def test_float_values(self):
        # Test with float values
        result = calc_initial_velocity(100.5, 5.2, 10.1)
        self.assertAlmostEqual(result, 47.98, places=2)  # Corrected Expected: 100.5 - (5.2*10.1)

if __name__ == "__main__":
    unittest.main()

