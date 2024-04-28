def calc_final_velocity(initial_velocity, deceleration_rate, time):
    """
    Calculate the final velocity of an object given its initial velocity,
    constant deceleration rate, and time period over which deceleration occurs.

    Parameters:
    initial_velocity (float): The velocity of the object at the start (m/s).
    deceleration_rate (float): The rate at which the object slows down (m/s²).
    time (float): The time over which the object decelerates (s).

    Returns:
    float: The final velocity of the object (m/s).
    """
    if not (isinstance(initial_velocity, (int, float)) and
            isinstance(deceleration_rate, (int, float)) and
            isinstance(time, (int, float))):
        raise ValueError("All parameters must be integers or floats.")
    if time < 0:
        raise ValueError("Time cannot be negative.")

    final_velocity = initial_velocity - (deceleration_rate * time)
    return final_velocity
