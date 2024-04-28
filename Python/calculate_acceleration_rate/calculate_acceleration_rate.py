def calc_acceleration_rate(initial_velocity, final_velocity, time):
    """
    Calculates the acceleration rate from initial to final velocity over a given time period.

    Parameters:
    initial_velocity (float): The initial velocity in units per second.
    final_velocity (float): The final velocity in units per second.
    time (float): The time over which the velocity change occurs, in seconds.

    Returns:
    float: The acceleration rate in units per second squared.

    Raises:
    ValueError: If time is zero, as acceleration cannot be calculated for zero time.
    """
    if time == 0:
        raise ValueError("Time cannot be zero for acceleration calculation.")
    
    acceleration_rate = (final_velocity - initial_velocity) / time
    return acceleration_rate

# Example usage:
try:
    accel_rate = calc_acceleration_rate(0, 100, 10)
    print(f"The acceleration rate is {accel_rate} units per second squared.")
except ValueError as e:
    print(e)
