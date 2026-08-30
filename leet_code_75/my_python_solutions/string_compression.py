# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.

# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter and should be ignored.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: 6
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].

# Example 2:
# Input: chars = ["a"]
# Output: 1
# Explanation: The only group is "a", which remains uncompressed since it is a single character.
# After modifying the input array in-place, the first character of chars should be ["a"].

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: 4
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
# After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].
 

# Constraints:
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
def compress(chars):
    # base case, chars is exactly size 1
    if len(chars) == 1:
        return 1
    # maintain a read and write index
    read_index = 0
    write_index = 0
    # maintain the current pattern count
    current_pattern_count = 1
    # process the patterns
    while (read_index < (len(chars) - 1)):
        # char[read_index] is the same as char[read_index + 1], increment the count
        if (chars[read_index] == chars[read_index + 1]):
            current_pattern_count += 1
            read_index += 1
        # they're not the same
        else:
            # if the character only occurs once
            if current_pattern_count == 1:
                # overwrite the char in w-index with r-index, and increment write
                chars[write_index] = chars[read_index]
                write_index += 1
            # the character occured more than once
            elif current_pattern_count > 1:
                # overwrite the char in w-index with r-index, and increment write
                chars[write_index] = chars[read_index]
                write_index += 1
                # for every digit in the count, overwrite the w-index with that digit
                for number in str(current_pattern_count):
                    chars[write_index] = number
                    write_index += 1
            # increment the read index, and reset the count pattern
            read_index += 1
            current_pattern_count = 1
        # we are at the end of the patterns
        if (read_index == (len(chars) - 1)):
            # overwrite the char in w-index with r-index, and increment write
            chars[write_index] = chars[read_index]
            write_index += 1
            # the character occured more than once
            if current_pattern_count > 1:
                # for every digit in the count, overwrite the w-index with that digit
                for number in str(current_pattern_count):
                    chars[write_index] = number
                    write_index += 1
    # return the write-index, which represent the length of chars
    return write_index

test_cases = [
    (
        ["a", "a", "b", "b", "c", "c", "c"],
        ["a", "2", "b", "2", "c", "3"]
    ),
    (
        ["a"],
        ["a"]
    ),
    (
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
        ["a", "b", "1", "2"]
    ),
    (
        ["a", "b", "c"],
        ["a", "b", "c"]
    ),
]

for i, (chars, expected) in enumerate(test_cases, 1):
    result = compress(chars)

    print(f"Test Case {i}:")
    print(f"Expected: {expected}")
    print(f"Result:   {chars[:result]}")
    print(f"Passed:   {chars[:result] == expected}")
    print()
