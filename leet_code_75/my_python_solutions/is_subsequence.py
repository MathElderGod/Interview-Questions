# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

def isSubsequence(s: str, t):
        # get the string length of both s and t
        stringSLength = len(s)
        stringTLength = len(t)
        # originally, should assume theyre not subsequences
        isSubsequence = False
        # if s is empty, return true, as the empty string is always a subsequence of ANY string
        if stringSLength == 0:
            return True
        # else if s is greater in length than t, return false
        elif stringSLength > stringTLength:
            return False
        # else if theyre the same length, return true or false depending on their comparison
        elif stringSLength == stringTLength:
            return s == t
        # else we can actively check if s is a subsequence of t
        else:
            # keep a pointer to string t
            j = 0
            # for each char in s
            for i in range(stringSLength):
                # if index i is not at the end of s, but index j is greater than t's length, and it was a subsequence so far, then 
                # return false as it is not a subsequence
                if (i < stringSLength) and (j > stringTLength - 1) and isSubsequence:
                    return False
                # iterate through string t
                while j < stringTLength:
                    # if the char for s at index i and t at index j are the same
                    if s[i] == t[j]:
                        # set subsequence to true
                        isSubsequence = True
                        # increment the pointer j for string t
                        j += 1
                        # break out the loop
                        break
                    # else theyre not the same chars
                    else:
                        # set subsequence to false
                        isSubsequence = False
                        # increment the pointer j for string t
                        j += 1
        # return the result of isSubsequence
        return isSubsequence

s = 'abc'
t = 'ahbgdc'
print(s + " is a subsequence of " + t + ": ", isSubsequence(s, t))

s = 'axc'
t = 'ahbgdc'
print(s + " is a subsequence of " + t + ": ", isSubsequence(s, t))

s = ''
t = 'ahbgdc'
print("''" + " is a subsequence of " + t + ": ", isSubsequence(s, t))

s = ''
t = ''
print("''" + " is a subsequence of " + "''" + ": ", isSubsequence(s, t))

s = 'abcd'
t = 'a'
print(s + " is a subsequence of " + t + ": ", isSubsequence(s, t))
