# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).


# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

def countBits(n):
    # set an array called ans of size n + 1 to all 0's
    ans = [0] * (n + 1)
    # iterate through every i in n, given 0 <= i <= n
    for i in range(n + 1):
        # if i is even, then set ans[i] to an existing value at index i divded by 2
        if i % 2 == 0:
            ans[i] = ans[i // 2]
        # else is is odd, then set ans[i] to an existing value at index [i - 1] incremented by 1
        else:
            ans[i] = ans[i - 1] + 1
    # return the array ans
    return ans

n = 2
print("n: ", n," Bit Counts: ", countBits(n), "\n")

n = 5
print("n: ", n," Bit Counts: ", countBits(n), "\n")

n = 7
print("n: ", n," Bit Counts: ", countBits(n))
