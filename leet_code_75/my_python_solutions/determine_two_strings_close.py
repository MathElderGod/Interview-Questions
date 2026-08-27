# Two strings are considered close if you can attain one from the other using the following operations:
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

# Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

# Constraints:
# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.
def closeStrings(word1, word2):
    # Base Case: if two words are not the same size, then they cannot be close
    if len(word1) != len(word2):
        return False
    # CASE 1: All characters must match between word 1 and word 2
    # use two hash maps, each containing characters and their frequencies from each word respectively
    word1_char_frequency_map = {}
    word2_char_frequency_map = {}
    # populate word 1 {char:freq} hashmap
    for char in word1:
        word1_char_frequency_map[char] = word1_char_frequency_map.get(char, 0) + 1
    # populate word 2 {char:freq} hashmap, while simultaneously checking if the current char is in hashmap for word 1
    for char in word2:
        # the words are not close, if word 1 and word 2 dont contain the same chars!
        if char not in word1_char_frequency_map:
            return False
        word2_char_frequency_map[char] = word2_char_frequency_map.get(char, 0) + 1
    # both frequency maps need to be the same size, else they can not be close
    if len(word1_char_frequency_map) != len(word2_char_frequency_map):
        return False
    # so far, word 1 and word 2, have the same chars but we need to verify the frequency counts
    # CASE 2: All frequency counts must match between word 1 and word 2 frequencies
    # create two hashmaps to map the frequencies from word 1 and word 2 to their counts
    word1_frequency_count_map = {}
    word2_frequency_count_map = {}
    # populate word 1 {freq:freq_count} hashmap
    for freq in word1_char_frequency_map.values():
        word1_frequency_count_map[freq] = word1_frequency_count_map.get(freq, 0) + 1
    # populate word 2 {freq:freq_count} hashmap, while simultaneously checking if the current freq is in {char:freq} hashmap for word 1
    for freq in word2_char_frequency_map.values():
        # the words are not close, if word 1 and word 2 dont have the same frequencies!
        if freq not in word1_frequency_count_map:
            return False
        word2_frequency_count_map[freq] = word2_frequency_count_map.get(freq, 0) + 1
    # the words are close iff their {freq:freq_count} hashmap's are the same
    is_close = word1_frequency_count_map == word2_frequency_count_map
    # return the result
    return is_close


test_cases = [
    ("abc", "bca"),
    ("a", "aa"),
    ("cabbba", "abbccc"),
    ("abbbzcf", "babzzcz"),
    ("abbzzca", "babzzcz"),
    ("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"),
]

for word1, word2 in test_cases:
    result = closeStrings(word1, word2)

    print("word1: ", word1)
    print("word2: ", word2)
    print("Output:", result)
    print()

