# You are given an integer array cost, where: cost[i] represents the cost of stepping on stair i.

# Once you pay the cost of a stair, you may climb either 1 or 2 stairs.
# You may start from either stair 0 or stair 1.

# Your goal is to reach the top of the staircase, which is just beyond the last element, while minimizing the total cost.

# Example 1
# cost = [10, 15, 20]

# The optimal path is:

# 15 → 20 → top

# But notice that you don't necessarily have to pay for the final stair if you jump over it.

# The answer is: 15
# Example 2
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

# The minimum cost is: 6

# Constraints
# 2 <= len(cost) <= 1000
# 0 <= cost[i] <= 999
# Your task

# Write:
# def minCostClimbingStairs(cost):
#     ...

# and return the minimum cost required to reach the top.

# This function finds the minimum cost to climb stairs given a cost array called
# costs for each i-th stair
def minCostClimbingStairs(cost):
    # get the length of the cost array
    cost_length = len(cost)
    # set the dp array to n elements, all consisting of 0
    dp = [0] * cost_length
    # set the starting values
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, cost_length):
        # dp[i] = minimum cost to reach stair i
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    # return the total min cost
    return min(dp[cost_length - 1], dp[cost_length - 2])

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print("Cost Array: ", cost, "\nMin Cost: ", minCostClimbingStairs(cost), "\n")
cost = [10, 15, 20]
print("Cost Array: ", cost, "\nMin Cost: ", minCostClimbingStairs(cost), "\n")
cost = [ 17, 83, 4, 91, 26, 7, 64, 13, 58, 2,
        99, 31, 6, 72, 15, 88, 3, 47, 21, 95,
        8, 54, 12, 76, 5, 63, 19, 84, 1, 39,
        67, 10, 92, 24, 6, 81, 14, 53, 9, 70,
        2, 61, 18, 97, 11, 45, 7, 86, 23, 4,
        69, 16, 78, 3, 52, 29, 90, 6, 35, 73,
        1, 57, 20, 82, 13, 49, 8, 94, 27, 5,
        71, 22, 63, 4, 89, 17, 36, 2, 75, 11,
        58, 14, 93, 6, 41, 28, 80, 3, 65, 19,
        7, 52, 1, 87, 24, 68, 5, 33, 91, 12 ]
print("Cost Array: ", cost, "\nMin Cost: ", minCostClimbingStairs(cost))

