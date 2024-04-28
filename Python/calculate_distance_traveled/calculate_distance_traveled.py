def calc_distance_traveled(initial_velocity, final_velocity, time):
    """
    Calculate the distance traveled under uniform acceleration.
    
    Parameters:
    initial_velocity (float): The initial velocity in units per time (e.g., meters per second).
    final_velocity (float): The final velocity in units per time (e.g., meters per second).
    time (float): The time duration in seconds over which the velocity is changing.
    
    Returns:
    float: The distance traveled in the same units as the velocity input (e.g., meters).
    
    Raises:
    ValueError: If time is negative.
    TypeError: If any of the inputs are not numbers.
    """
    if not all(isinstance(x, (int, float)) for x in [initial_velocity, final_velocity, time]):
        raise TypeError("All parameters should be numbers.")
    
    if time < 0:
        raise ValueError("Time cannot be negative.")
    
    distance_traveled = ((initial_velocity + final_velocity) / 2) * time
    return distance_traveled

# Example usage:
try:
    print(calc_distance_traveled(10, 20, 5))  # Example: Initial velocity = 10 m/s, final velocity = 20 m/s, time = 5 s
except Exception as e:
    print(e)
