# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
def decodeString(s):
    # define an empty stack
    stack = []
    # set an empty string for the decoded string
    decoded_string = ""
    # set the current count to 0
    current_count = 0
    for current_char in s:
        # the current character of the string is in the alphabet
        if current_char.isalpha():
            # append the current char to the decoded string
            decoded_string += current_char
        # the current char is a number
        elif current_char.isdigit():
            # if the count hasn't been set, set it to the current number
            if current_count == 0:
                current_count = int(current_char)
            # else set it to the prior count shifted to the next decimal plus the current number
            else:
                current_count = (10 * current_count) + int(current_char)
        # the current char represent the end of the prior state
        elif current_char == "[":
            # save the prior state
            prior_state = (decoded_string, current_count)
            stack.append(prior_state)
            # reset the decoded string and the current count
            decoded_string = ""
            current_count = 0
        # else we have reach the end of our processing
        else:
            # get the prior state
            prior_state = stack.pop()
            # the decoded string is: the prior string + (decoded string repeated prior count times)
            decoded_string = prior_state[0] + (prior_state[1] * decoded_string)
    # return the decoded string
    return decoded_string

# Test cases
test_cases = [
    "3[a]2[bc]",
    "3[a2[c]]",
    "2[abc]3[cd]ef"
]

for s in test_cases:
    result = decodeString(s)

    print("Input:  ", s)
    print("Output: ", result, "\n")
