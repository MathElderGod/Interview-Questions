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
    # get the length of the array
    array_length = len(arr)
    # make a dictionary that maps (key) direct number values and (values) number of occurences of those values
    # ex: { Key --> 1: Value --> 3}, the number 1 (key) has 3 (value) occurences.
    number_of_occurences_mapping = {}
    # populate the dictionary with each number from array with the count set to 0
    for i in range(array_length):
        number_of_occurences_mapping.update({arr[i]: 0})
    # increment the count for each key's value, if the key number is observed in the array
    for i in range(array_length):
        number_of_occurences_mapping[arr[i]] = number_of_occurences_mapping[arr[i]] + 1
    # make an empty list of occurences
    unique_occurences = []
    # iterate through each value in the dictionary, which is the total number of occurences of each key number
    for total_occurences_of_current_value in number_of_occurences_mapping.values():
        # if the total number of occurences is truly unique, then append the value to unique occurences array
        if total_occurences_of_current_value not in unique_occurences:
            unique_occurences.append(total_occurences_of_current_value)
        # else, the total number of occurences has already been observed, so return false
        else:
            return False
    # otherwise, return true as we have truly seen a unique number of occurences per each key number
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
