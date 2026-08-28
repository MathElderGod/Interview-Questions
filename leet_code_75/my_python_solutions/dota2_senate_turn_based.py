# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".


# Example 1:
# Input: senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

# Example 2:
# Input: senate = "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And the third senator comes from Dire and he can ban the first senator's right in round 1.
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
# from collections import deque

from collections import deque
def predictPartyVictory(senate):
    # two deques
    # track the current senator(s) who have yet to take their turn
    current_senator = deque(senate[0])
    # track the senators to the right of the current senator(s)
    senator_to_the_right = deque(senate[1:])
    # their must always be a senator to the right who has not taken a turn
    while senator_to_the_right:
        # current senator and the senator to the right are in the same party
        # thus, append the senator to the right to the current senators
        if current_senator[0] == senator_to_the_right[0]:
            current_senator.append(senator_to_the_right.popleft())
        # the current senator and the senator to the right are in different parties
        else:
            # ban the opposing senator to the right
            senator_to_the_right.popleft()
            # append the current senator to the back of the senators to the right
            senator_to_the_right.append(current_senator.popleft())
            # edge case: current senators is empty,
            if not current_senator:
                # kick a senator to the right to be the current senator
                current_senator.append(senator_to_the_right.popleft())
    # return Dire if the current senator is in dire, otherwise Radiant
    return "Dire" if ("D" in current_senator) else "Radiant"

senate = "RD"
print("Senate: ", senate)
print("Winning Party: ", predictPartyVictory(senate), "\n")    # Radiant
senate = "RDD"
print("Senate: ", senate)
print("Winning Party: ", predictPartyVictory(senate), "\n")    # Radiant
