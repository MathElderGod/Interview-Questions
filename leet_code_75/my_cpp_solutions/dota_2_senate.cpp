//  In the world of Dota2, there are two parties : the Radiant and the Dire.
//
//  The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round - 
//  based procedure. In each round, each senator can exercise one of the two rights :
//
//  Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
//  Announce the victory : If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
//  Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, 
//  the size of the given string will be n.
//
//  The round - based procedure starts from the first senator to the last senator in the given order.This procedure will last until the end of voting. All the senators who have 
//  lost their rights will be skipped during the procedure.
//
//  Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game.
//  The output should be "Radiant" or "Dire".
//
//
//
//  Example 1:
//
//  Input: senate = "RD"
//  Output : "Radiant"
//  Explanation :
//    The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
//    And the second senator can't exercise any rights anymore since his right has been banned. 
//    And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
//  
//  Example 2 :
//
//    Input : senate = "RDD"
//    Output : "Dire"
//    Explanation :
//    The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
//    And the second senator can't exercise any rights anymore since his right has been banned. 
//    And the third senator comes from Dire and he can ban the first senator's right in round 1. 
//    And in round 2, the third senator can just announce the victory since he is the only guy 
//    in the senate who can vote.
#include <iostream>
#include <queue>
#include <string>
using namespace std;

class DotaParty {
public:
    string predictPartyVictory(string senate) {
        // keep track of the current senators
        queue<char> currentSenators;
        // keep track of voting senators
        queue<char> votingSenators;
        // get the length of the senate
        int senateLength = senate.length();
        // populate the current senators
        for (int i = 0; i < senateLength; i++) {
            currentSenators.push(senate[i]);
        }
        // pick the first senator from the current senate to vote
        votingSenators.push(currentSenators.front());
        currentSenators.pop();
        // go through the dota 2 rounds until there are no more senators of the opposing party
        while (!currentSenators.empty()) {
            char votingSenator = votingSenators.front();
            char currentSenator = currentSenators.front();
            // if the senators are on opposing parties, the voting senator bans the current senator
            if (votingSenator != currentSenator) {
                // ban the current senator
                currentSenators.pop();
                // push the voting senator to the back of the current senate
                currentSenators.push(votingSenator);
                votingSenators.pop();
                // if there are no voting senators, pick one to vote from the current senators
                if (votingSenators.empty()) {
                    votingSenators.push(currentSenators.front());
                    currentSenators.pop();
                }
                // else the senators are in the same party, so push the current senator to the voting senate
            } else {
                votingSenators.push(currentSenator);
                currentSenators.pop();
            }
        }
        // the current senate is thus empty, so return who the winning party is from the voting senate. 
        return (votingSenators.front() == 'D') ? "Dire" : "Radiant";
    }
};

int main(void) {
    cout << "Type in a senate combination of D's and R's to Play Dota 2 and see the winner! (Else Type q to quit!): ";
    string senate;
    cin >> senate;
    DotaParty currentDota;
    while (senate.compare("q") != 0) {
        cout << "The winning party is: " << currentDota.predictPartyVictory(senate) << endl;
        cout << "Type in a senate combination of D's and R's to Play Dota 2 and see the winner! (Else Type q to quit!): ";
        senate = "";
        cin >> senate;
    }
    return EXIT_SUCCESS;
}
