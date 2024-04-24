#checks for the largest number in a list
def largest_num(nums):
    if not nums:  # Check if the list is empty
        return None  # or raise an exception, or handle it as appropriate
    largest = nums[0]  # Initialize `largest` to the first element in the list
    for num in nums:
        if num > largest:
            largest = num
    return largest
