# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

# Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
def uniqueOccurrences(arr):
    # basically using a hashmap and set together
    # make a (hashmap) dictionary that maps (key) number values and (values) number of occurrences of those values
    # ex: { Key --> 1: Value --> 3}, the number 1 (key) has 3 (value) occurrences.
    number_of_occurrences_mapping = {}
    # populate the dictionary
    for number in arr:
        # get the current number from the dictionary, if it doesnt exist, set it its frequency to 1,
        # else increment its frequency by 1 if it exists
        number_of_occurrences_mapping[number] = (
            number_of_occurrences_mapping.get(number, 0) + 1
        )
    # make an empty set of occurrences
    unique_occurrences = set()
    # iterate through each value in the (hashmap) dictionary, which is the frequency of each number
    for freq in number_of_occurrences_mapping.values():
        # return false if the frequency has already been observed
        if freq in unique_occurrences:
            return False
        unique_occurrences.add(freq)
    # return true, as every frequency is unique
    return True

arr = [1, 2, 2, 1, 1, 3]
print("Current Array: ", arr) 
print("Output: ", uniqueOccurrences(arr)) 
print("Expected: True\n")

arr = [1, 2]
print("Current Array: ", arr) 
print("Output: ", uniqueOccurrences(arr))
print("Expected: False\n")

arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print("Current Array: ", arr) 
print("Output: ", uniqueOccurrences(arr)) 
print("Expected: True")
