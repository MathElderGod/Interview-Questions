/** 

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false
    

    Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

*/

public class IsSubsequence {
    public boolean isSubsequence(String s, String t) {
        // assume string s and t are not subsequences at first
        boolean isSubsequence = false;
        // extract the lengths of both strings
        int stringSLength = s.length();
        int stringTLength = t.length();

        // if the string s is the empty string, just return true, as empty string is a subsequence of all strings
        if(stringSLength == 0){
            return true;
        // else if s is greater than t in length, return false
        } else if(stringSLength > stringTLength){
            return false;
        // else if s and t are the same length, return true if theyre the same string, else false
        } else if(stringSLength == stringTLength){
            return s == t;
        // else s could be a subsequence
        } else {
            int j = 0;
            // iterate through each char of string s
            for(int i = 0; i < stringSLength; i++){
                // if j for t is out of bounds, and i for s is not, and isSubsequence is true, then its not a subsequence
                if((j > stringTLength - 1) && (i < stringSLength) && isSubsequence){
                    return false;
                }
                // for each char in t
                while(j < stringTLength){
                    // if i for s and j for t match, set is subsequence to true, increment and break out the loop
                    if(s.charAt(i) == t.charAt(j)){
                        isSubsequence = true;
                        j++;
                        break;
                    // else theyre not, increment, and continue with the loop
                    } else {
                        isSubsequence = false;
                        j++;
                    }
                }
            }
            // return isSubsequence result
            return isSubsequence;
        }
    }
    public static void main (String args[]) {
        IsSubsequence isSub = new IsSubsequence();
        
        String s = "abc";
        String t = "ahbgdc";
        System.out.println(s + " is a subsequence of " + t + ": " + isSub.isSubsequence(s, t));
        
        s = "axc";
        t = "ahbgdc";
        System.out.println(s + " is a subsequence of " + t + ": " + isSub.isSubsequence(s, t));
        
        s = "";
        t = "ahbgdc";
        System.out.println("''" + " is a subsequence of " + t + ": " + isSub.isSubsequence(s, t));
        
        s = "";
        t = "";
        System.out.println("''" + " is a subsequence of " + "''" + ": " + isSub.isSubsequence(s, t));
        
        s = "abcdfg";
        t = "ahbg";
        System.out.println(s + " is a subsequence of " + t + ": " + isSub.isSubsequence(s, t));
    }
}
