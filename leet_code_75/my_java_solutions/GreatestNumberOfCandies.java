import java.util.*;
/**

    There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.

    Example 1:
    Input: candies = [2,3,5,1,3], extraCandies = 3
    Output: [true,true,true,false,true] 
    Explanation: If you give all extraCandies to:
    - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
    - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
    - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
    - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

    Example 2:
    Input: candies = [4,2,1,1,2], extraCandies = 1
    Output: [true,false,false,false,false] 
    Explanation: There is only 1 extra candy.
    Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

    Example 3:
    Input: candies = [12,1,12], extraCandies = 10
    Output: [true,false,true]
    
    Constraints:
    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50

 */

class GreatestNumberOfCandies {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // get the number of kids from the candies array
        int numKids = candies.length;
        // create an empty boolean array list
        List<Boolean> hasGreatestCandiesArray = new ArrayList<Boolean>();
        
        // get the max number of candies from the array
        int maxCandies = 0;
        // for every kid
        for(int i = 0; i < numKids; i++){
            // find the greatest number of candies possessed
            if (maxCandies < candies[i]) {
                maxCandies = candies[i];
            }
        }
        
        // set the current candy count
        int currentCandyCount = 0;
        // for every kid
        for(int i = 0; i < numKids; i++){
            // set the current candy count by setting it to the number of candies a kid has + the number of extra candies
            currentCandyCount = candies[i] + extraCandies;
            // if the current candy count is at least the number of max candies, enter
            if(currentCandyCount >= maxCandies){
                // set the current kids greatest candies held value to true
                hasGreatestCandiesArray.add(true);
                // reset the current count
                currentCandyCount = 0;
                // else the current kid does not have the greatest number of candies
            } else {
                // set the current kids greatest candies held value to false
                hasGreatestCandiesArray.add(false);
                // reset the count
                currentCandyCount = 0;
            }
        }
        // return the greatest number of candies held per kid boolean array
        return hasGreatestCandiesArray;
    }
    public static void main(String args[]){
        GreatestNumberOfCandies gnoc = new GreatestNumberOfCandies();
        
        int candies[] = {12, 1, 12};
        int extraCandies = 10;
        System.out.println("Candies: [12, 1, 12] - Extra Candies: " +
        extraCandies);
        System.out.println("Expected: [true, false, true] - Result: " +
        gnoc.kidsWithCandies(candies, extraCandies) + "\n");
        
        int candies1[] = {4, 2, 1, 1, 2};
        extraCandies = 1;
        System.out.println("Candies: [4, 2, 1, 1, 2] - Extra Candies: " +
        extraCandies);
        System.out.println("Expected: [true, false, false, false, false] - Result: " +
        gnoc.kidsWithCandies(candies1, extraCandies) + "\n");
        
        int candies2[] = {2, 3, 5, 1, 3};
        extraCandies = 3;
        System.out.println("Candies: [2, 3, 5, 1, 3] - Extra Candies: " +
        extraCandies);
        System.out.println("Expected: [true, true, true, false, true] - Result: " +
        gnoc.kidsWithCandies(candies2, extraCandies));
    }
}
