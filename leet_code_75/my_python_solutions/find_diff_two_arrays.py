# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

# Example 2:
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000
def findDifference(nums1, nums2):
    # make empty lists
    answers = []
    answers1 = []
    answers2 = []
    # get the length of nums1
    nums1_length = len(nums1)
    # get the length of nums2
    nums2_length = len(nums2)
    # for every element in nums 1
    for i in range(nums1_length):
        # if nums at the i-th index is not in nums2 and answers1 list, then append it to answers1
        if nums1[i] not in nums2 and nums1[i] not in answers1:
            answers1.append(nums1[i])
    # for every element in nums 2
    for j in range(nums2_length):
        # if nums at the j-th index is not in nums1 and answers2 list, then append it to answers2
        if nums2[j] not in nums1 and nums2[j] not in answers2:
            answers2.append(nums2[j])
    # append both lists to answers list
    answers.append(answers1)
    answers.append(answers2)
    # return the answers
    return answers

nums1 = [1,2,3]
nums2 = [2,4,6]
print("nums1: ", nums1)
print("nums2: ", nums2)
print("Output:  ", findDifference(nums1, nums2))
print("Expected: [[1, 3], [4, 6]]\n")

nums1 = [1,2,3,3]
nums2 = [1,1,2,2] 
print("nums1: ", nums1) 
print("nums2: ", nums2)
print("Output:  ", findDifference(nums1, nums2)) 
print("Expected: [[3], []]")
