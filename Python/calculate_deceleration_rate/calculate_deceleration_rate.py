def calc_deceleration_rate(initial_velocity, final_velocity, time):
    """
    Calculates the deceleration rate given the initial and final velocities, and time period.

    Parameters:
    initial_velocity (float): The starting velocity in units per time (e.g., meters per second).
    final_velocity (float): The ending velocity in units per time.
    time (float): The time period over which the velocity change occurs in seconds.

    Returns:
    float: The deceleration rate in units per time squared (e.g., meters per second squared).

    Raises:
    ValueError: If time is zero, or if initial_velocity or final_velocity are not greater than zero,
                or if initial_velocity is less than final_velocity.
    """
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
