#checks for the largest number in a list
def largest_num(nums):
    largest = 0
    for num in nums:
        if num > largest:
            largest = num
    return largest