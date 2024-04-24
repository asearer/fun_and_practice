def find_smallest(numbers):
    """
    Finds and returns the smallest number in a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    int/float: The smallest number in the list, or None if the list is empty.
    """
    if not numbers:  # Check if the list is empty
        return None  # Return None if the list is empty to handle gracefully
    return min(numbers)
