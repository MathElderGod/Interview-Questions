# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.
# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537

# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
def tribonacci(n):
    # T_0 = 0, T_1 = 1, T_2 = 1, and T_n+3 = T_n + T_n+1 + T_n+2 for n >= 0.
    # base cases for 0 <= n <= 2
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    # base case for all n, such that n >= 3
    else:
        # set up the current tribonacci sum to 0, to represent the n-th tribonacci number
        current_tribo = 0
        # populate the first 3 tribonacci numbers
        first_tribo = 0
        second_tribo = 1
        third_tribo = 1
        # for every i in range [3, n + 1), calculate the current i-th tribonacci number.
        # current_tribo represents the sum (current tribonacci number) from the last 3 
        # (tribonacci numbers) sums already calculated
        for i in range(3, n + 1):
            # T_n = T_n-3 + T_n-2 + T_n-1 for n >= 0
            current_tribo = third_tribo + second_tribo + first_tribo
            # update the last 3 tribonacci number
            first_tribo = second_tribo
            second_tribo = third_tribo
            third_tribo = current_tribo
    # return the n-th tribonacci number
    return current_tribo

user_input = (int)(input("Enter a number to caclulate the n-th tribonacci number (Type -1 to quit.): "))

while user_input != -1:
    print("The ", user_input, "- th tribonacci number is: ", tribonacci(user_input))
    user_input =  (int)(input("Enter a number to calculate the n-th tribonacci number (Type -1 to quit.): "))
