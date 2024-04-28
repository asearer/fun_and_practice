def calc_initial_velocity(final_velocity: float, acceleration_rate: float, time: float) -> float:
    """
    Calculate the initial velocity of an object given its final velocity,
    constant acceleration, and the time over which the acceleration is applied.

    Parameters:
    - final_velocity (float): The final velocity of the object in meters per second (m/s).
    - acceleration_rate (float): The acceleration rate in meters per second squared (m/s^2).
    - time (float): The time over which the acceleration was applied in seconds (s).

    Returns:
    - float: The initial velocity of the object in meters per second (m/s).
    """
    initial_velocity = final_velocity - (acceleration_rate * time)
    return initial_velocity
