# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


def productExceptSelf(nums):
    # maintain the left product
    product_left = 1
    # keep a list to store the answers
    answers = []
    # calculate the left products for every index location
    for i in range(len(nums)):
        answers.append(product_left)
        product_left = nums[i] * product_left
    # maintain the right product
    product_right = 1
    # calculate the overall product of the elements at i, not including i
    for i in reversed(range(len(nums))):
        # overall product at i is product left * product right
        answers[i] = answers[i] * product_right
        # update the right products, to the product of all numbers to the
        # right and the current right product
        product_right = nums[i] * product_right
    # return array of products
    return answers


test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([1, 1, 0, -3, 3], [0, 0, -9, 0, 0]),
]

for i, (nums, expected) in enumerate(test_cases, 1):
    result = productExceptSelf(nums)

    print(f"Test Case {i}:")
    print(f"Input:    {nums}")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    print(f"Passed:   {result == expected}")
    print()

