# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
# from collections import deque
from collections import deque
def reverseWords(s):
    # make a deque for current strings
    current_words = deque()
    # make a list for reversed strings
    reversed_words = []
    # set a counter for the current index 
    i = 0
    # process the string
    while i < len(s):
        # set the current word to the empty string
        current_word = ""
        # as long as there is a char to process and its not a space, process the word
        while (i < len(s)) and (s[i] != " "):
            current_word += s[i]
            i += 1
        # if the word is not empty, append it to the current words
        if current_word != "":
            current_words.append(current_word)
        i += 1
    # append the words in reverse order to reversed strings
    while current_words:
        reversed_words.append(current_words.pop())
    # return a string representation of the reversed words
    return " ".join(reversed_words)
# Time Complexity: 
# O(n) because we process each character in the input string once. 
# Building the words takes O(n) total. 
# Popping all K words from the deque takes O(k). 
# Joining the K words into the final string takes O(n), since we must 
# construct the resulting string. 
# Since k <= n, the overall runtime is O(n). 

# Space Complexity: 
# O(n) because we store all K words in the deque and then store them 
# again in the reversed_words list. 
# The total number of characters stored across all words is O(n).
# Test cases

s = "a good   example"
print(s)
print(reverseWords(s))
print()

s = "  hello world  "
print(s)
print(reverseWords(s))
print()

s = "the sky is blue"
print(s)
print(reverseWords(s))
print()

s = "hello"
print(s)
print(reverseWords(s))
print()

s = "   hello   "
print(s)
print(reverseWords(s))
print()

s = "hello     world"
print(s)
print(reverseWords(s))
print()

s = "a"
print(s)
print(reverseWords(s))
print()

s = "one two three four five"
print(s)
print(reverseWords(s))
print()

s = "  multiple    spaces   everywhere  "
print(s)
print(reverseWords(s))
print()
