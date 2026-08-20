# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Example 1:
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


# Constraints:
# 1 <= t <= 109
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.

# Using a double ended queue for the implementation
from collections import deque


class RecentCounter:
    def __init__(self):
        # define the lower bound of the current request t
        # define the current requests by setting it to an empty lists
        self.lower_bound_of_current_request = 0
        self.current_requests = deque([])

    def ping(self, t: int) -> int:
        # redetermine the current lower bound given the last 3000 milliseconds of the current request t
        self.lower_bound_of_current_request = t - 3000
        # populate the requests list by appending to the beginning of the queue
        self.current_requests.appendleft(t)
        # set the oldest request
        oldest_request = self.current_requests.pop()
        # if the oldest request is less than the lower bound
        while oldest_request < self.lower_bound_of_current_request:
            # update the oldest request
            oldest_request = self.current_requests.pop()
        # the oldest is greater than or equals to the lower bound, so we need to add it back
        self.current_requests.append(oldest_request)
        # return the current number of requests that are in the specified range [t - 3000, t]
        return len(self.current_requests)

