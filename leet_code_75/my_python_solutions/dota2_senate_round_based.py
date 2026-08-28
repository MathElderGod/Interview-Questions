
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
    # one for dire senator positions
    dire_senators = deque()
    # one for radiant senator positions
    radiant_senators = deque()
    # populate the positions in each party, respectively
    for i in range(len(senate)):
        if senate[i] == "D":
            dire_senators.append(i)
        else:
            radiant_senators.append(i)
    # keep tack of the next round
    next_round = len(senate)
    # while both parties still have senators to cast votes
    while dire_senators and radiant_senators:
        # the dire senator comes first, and can cast a vote
        if dire_senators[0] < radiant_senators[0]:
            # ban the radiant senator
            radiant_senators.popleft()
            # push the dire senator to the next round
            dire_senators.append(dire_senators.popleft() + next_round)
        # the radiant senator comes first, and can cast a vote
        else:
            # ban the dire senator
            dire_senators.popleft()
            # push the radiant senator to the next round
            radiant_senators.append(radiant_senators.popleft() + next_round)
    # return dire if the radiant party has no senators, else radiant
    return "Dire" if not radiant_senators else "Radiant"

senate = "RD"
print("Senate: ", senate)
print("Winning Party: ", predictPartyVictory(senate), "\n")    # Radiant
senate = "RDD"
print("Senate: ", senate)
print("Winning Party: ", predictPartyVictory(senate), "\n")    # Radiant
