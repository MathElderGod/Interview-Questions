# You are given an array where: nums[i] represents the amount of money in house i.

# You want to maximize the amount of money you can rob.

# Constraint: You cannot rob two adjacent houses.

# Example:
# nums = [2, 7, 9, 3, 1]

# Optimal:
# 2 + 9 + 1 = 12

# Return: 12

# Constraints
# 1 <= len(nums) <= 1000
# 0 <= nums[i] <= 10,000
# Your task

# Write:
# def rob(nums):
#     ...

def rob(nums):
    # get the size of nums
    n = len(nums)
    if n == 1:
        return nums[0]
    # set dp to have 0 n elements
    dp = [0] * n
    # two choices, either rob house i, or dont rob it
    # first house is robbed
    dp[0] = nums[0]
    # determine whether the first or 2nd house should be robbed
    dp[1] = max(nums[0], nums[1]) 
    for i in range(2, n):
        # dp[i] represents the maximum amount of money
        # that can be robbed from houses 0 through i, inclusive.
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    # return the max amount of money robbed
    return dp[n - 1]
nums = [2, 7, 9, 3, 1]
print("Nums: ", nums, "\nMax Money to Rob: ", rob(nums), "\n")
nums = [
    83, 17, 94, 42, 7, 91, 36, 88, 14, 73,
    65, 9, 97, 31, 56, 12, 84, 45, 78, 3,
    92, 26, 61, 99, 18, 72, 5, 87, 34, 76,
    11, 95, 28, 63, 8, 89, 41, 54, 96, 22,
    69, 6, 81, 37, 93, 15, 58, 100, 24, 67,
    4, 86, 32, 74, 19, 98, 43, 52, 79, 10,
    90, 27, 62, 85, 13, 71, 39, 57, 99, 21,
    68, 5, 94, 30, 82, 16, 73, 44, 91, 7,
    59, 88, 25, 64, 97, 12, 78, 35, 83, 3,
    70, 46, 95, 18, 61, 89, 9, 77, 29, 100
]
print("Nums: ", nums, "\nMax Money to Rob: ", rob(nums), "\n")
nums = [2]
print("Nums: ", nums, "\nMax Money to Rob: ", rob(nums))
