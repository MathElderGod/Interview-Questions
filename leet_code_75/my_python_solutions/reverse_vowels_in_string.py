# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


def reverseVowels(s):
    # create an array from the string of characters
    character_array = list(s)
    # extract the length of the string
    input_length = len(s)
    # maintain a vowels array to check if a character is a vowel
    vowels = ["a", "e", "i", "o", "u"]
    # pointer to the first character in the string
    i = 0
    # pointer to the second character in the string
    j = input_length - 1
    # while the first and second pointer do not exceed their current locations, enter
    while i <= j:
        # get the first character
        first_char = character_array[i].lower()
        # get the second characeter
        second_char = character_array[j].lower()
        # if the first character is a vowel, and the second characeter is a vowel, swap them
        if first_char in vowels and second_char in vowels:
            # temporarily store the first character
            temp = character_array[i]
            # set the first to the second
            character_array[i] = character_array[j]
            # set the second to the first via the temp
            character_array[j] = temp
            # move both pointers respectfully
            i += 1
            j -= 1
        # else if the first character is a vowel, but the second character is not
        elif first_char in vowels and second_char not in vowels:
            # move the pointer for the second character
            j -= 1
        # else if the first character is not a vowel, but the second character is
        elif first_char not in vowels and second_char in vowels:
            # move the pointer for the first character
            i += 1
        # else none are vowels
        else:
            # move both pointers to the next characters respectfully
            i += 1
            j -= 1
    # extract the reversed vowels string
    reversed_vowels_string = "".join(character_array)
    # return the reversed string
    return reversed_vowels_string

current_string = "IceCreAm"
print("Original String:", current_string)
print("Reversed String: ",  reverseVowels(current_string), "\n")


current_string = "leetcode"
print("Original String:", current_string)
print("Reversed String: ",  reverseVowels(current_string))
