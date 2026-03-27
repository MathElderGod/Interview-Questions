# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

def moveZeroes(nums):
         
        numsLength = len(nums)
        # if nums length is 1 then return from the function
        if numsLength == 1:
            return None

        # two pointers since nums length is greater than 1
        i = 0
        j = 1

        # keep iterating through nums
        while i != numsLength - 1:
            # case 1: i is zero and j is nonzero, so swap their positions
            if j <= numsLength - 1 and nums[i] == 0 and nums[j] != 0 :
                # swap values
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                # set the pointers accordingly
                i += 1
                j = i + 1
            # case 2: i is 0 and j is 0, increment j only to find the next nonzero
            elif j <= numsLength - 1 and nums[i] == 0 and nums[j] == 0 :
                j += 1
            # last case is to increment i and set j to i + 1
            else:
                i += 1
                j = i + 1

nums_array = [0, 1, 0, 3, 12]
moveZeroes(nums_array)
print("Expected: [1, 3, 12, 0, 0] " + " Result: ", nums_array)

nums_array = [0, 5, 0, 1, 0, 2, 15, 0, 0, 0, 5]
moveZeroes(nums_array)
print("Expected: [5, 1, 2, 15, 5, 0, 0, 0, 0, 0, 0] " + " Result: ", nums_array)

nums_array = [0, 0]
moveZeroes(nums_array)
print("Expected: [0, 0] " + " Result: ", nums_array)

nums_array = [1, 0]
moveZeroes(nums_array)
print("Expected: [1, 0] " + " Result: ", nums_array)


nums_array = [0, 5]
moveZeroes(nums_array)
print("Expected: [5, 0] " + " Result: ", nums_array)

nums_array = [10]
moveZeroes(nums_array)
print("Expected: [10] " + " Result: ", nums_array)
