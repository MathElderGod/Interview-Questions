# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999


def minCostClimbingStairs(cost):
    cost_length = len(cost)
    # base case for cost being size 0 or 1 (just skip the step or do nothing)
    if (cost_length == 0) or (cost_length == 1):
        return 0
    # base case for cost being size 2 or greater
    else:
        # keep track of the current cost
        current_cost = 0
        # step_one_total represents cost[0], as we take the first step
        step_one_total = cost[0]
        # step_two_total represents cost[1], as we took the second step, and not the first
        step_two_total = cost[1]
        # current_cost represents the total minimum cost accrued reaching step i plus the current cost
        for i in range(2, cost_length):
            current_cost = cost[i] + min(step_one_total, step_two_total)
            # update the total costs
            # Shift the two most recent DP states forward.
            step_one_total = step_two_total
            step_two_total = current_cost
        # return the total minimum cost of reaching the last two steps
        return min(step_one_total, step_two_total)

# Test cases
test_cases = [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
]


for cost in test_cases:
    result = minCostClimbingStairs(cost)

    print("Input:   ", cost)
    print("Output:  ", result, "\n")
