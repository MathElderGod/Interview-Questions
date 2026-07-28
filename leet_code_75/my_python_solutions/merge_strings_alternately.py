# You are given two strings word1 and word2. Merge the strings by adding letters 
# in alternating order, starting with word1. If a string is longer than the other, 
# append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 
#Constraints:

#1 <= word1.length, word2.length <= 100
#word1 and word2 consist of lowercase English letters.
def mergeAlternately(word1, word2):
        # declare and intialize an empty string
        merged_string = ""
        # keep track of the index
        current_idx = 0
        # take the lengths early, to stop calling the length function
        word1_length = len(word1)
        word2_length = len(word2)

        # iterate through the length of word 1
        for current_idx in range(word1_length):
            # if the current index is not out of bounds for either of the words
            if current_idx < word1_length and current_idx < word2_length:
                # merge the characters
                merged_string += word1[current_idx]
                merged_string += word2[current_idx]
            else:
                # the index is out of bounds for at least 1 word
                break

        # if word 1 is bigger
        if word1_length > word2_length:
            # append the sliced remainder of word1 to the merged string
            merged_string += word1[current_idx:word1_length]
            # return the merged string
            return merged_string
        # else if word 2 is bigger
        elif word2_length > word1_length:
            # we need to append the sliced remainder at current index + 1 to the merged string, 
            # because the current index was not incremented in the for loop
            merged_string += word2[current_idx + 1:word2_length]
            # return the merged string
            return merged_string
        # they are the same size
        else:
            # return the merged string
            return merged_string

# some tests
word1 = 'ab'
word2 = 'pqrs'
merged_string = mergeAlternately(word1, word2)
print("Test Case 1 Result  : " + merged_string)
print("Test Case 1 Expected: " + "apbqrs" + "\n")

word1 = 'abcd'
word2 = 'pq'
merged_string = mergeAlternately(word1, word2)
print("Test Case 2 Result  : " + merged_string)
print("Test Case 2 Expected: " + "apbqcd" + "\n")

word1 = 'abc'
word2 = 'pqr'
merged_string = mergeAlternately(word1, word2)
print("Test Case 3 Result  : " + merged_string)
print("Test Case 3 Expected: " + "apbqcr")

word1 = 'Notepad'
word2 = 'Alex'
merged_string = mergeAlternately(word1, word2)
print("Test Case 3 Result  : " + merged_string)
print("Test Case 3 Expected: " + "NAolteexpad")
