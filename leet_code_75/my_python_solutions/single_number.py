# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

def singleNumber(nums):
    # set a variable to store the unique number
    unique_number = 0
    # for every number in nums
    for some_number in nums:
        # xor all the numbers together to extract the unqiue number
        unique_number = unique_number ^ some_number
    # return the unique number
    return unique_number

nums = [2, 2, 1]
print("Nums: ", nums, "\nUnique Number: ", singleNumber(nums), "\n")

nums = [4,1,2,1,2]
print("Nums: ", nums, "\nUnique Number: ", singleNumber(nums), "\n")

nums = [1]
print("Nums: ", nums, "\nUnique Number: ", singleNumber(nums))
