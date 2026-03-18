/**
  * You are given two strings word1 and word2. Merge the strings by adding letters in 
  * alternating order, starting with word1. If a string is longer than the other, 
  * append the additional letters onto the end of the merged string. Return the merged string.
  *
  * Example 1:
  * Input: word1 = "abc", word2 = "pqr"
  * Output: "apbqcr"
  * Explanation: The merged string will be merged as so:
  * word1:  a   b   c
  * word2:    p   q   r
  * merged: a p b q c r
  *
  * Example 2:
  * Input: word1 = "ab", word2 = "pqrs"
  * Output: "apbqrs"
  * Explanation: Notice that as word2 is longer, "rs" is appended to the end.
  * word1:  a   b 
  * word2:    p   q   r   s
  * merged: a p b q   r   s
  * 
  * Example 3:
  * Input: word1 = "abcd", word2 = "pq"
  * Output: "apbqcd"
  * Explanation: Notice that as word1 is longer, "cd" is appended to the end.
  * word1:  a   b   c   d
  * word2:    p   q 
  * merged: a p b q c   d
 
  * Constraints:
  * 1 less than equal to word1.length, word2.length less than equal to  100
  * word1 and word2 consist of lowercase English letters.
  */

class MergeStringsAlternately {

    /** 
      * This method merges two strings alternating bewtween characters, and appends the remainder
      * of the longer string to the merged string:
      *
      * @param word1 a string to merge
      * @param word2 another string to merge
      *
      * @return mergedString a string merged from word1 and word2 in an alternate manner
      *
      */
    public String mergeAlternately(String word1, String word2) {
        // get the word length to ensure not to call length() as it is expensive.
        int word1Length = word1.length();
        int word2Length = word2.length();
        // Variable to store merged string
        String mergedString = "";
        // keep track of the index
        int i;
        // iterate throught any word length
        for(i = 0; i < word1Length; i++){
            // if the index is out of bounds for one of the words
            if(i > word1Length - 1 || i > word2Length - 1){
                // break out the code
                break;
            }
            mergedString += word1.charAt(i);
            mergedString += word2.charAt(i);
        }

        // 3 cases
        // word 1 is longer, thus append the remaining portion of word 1 and return it
        if(word1Length > word2Length){
            mergedString += word1.substring(i, word1Length);
            return mergedString;
        // else if word 2 is longer, append the remainder of word 2 mand return it
        }else if(word2Length > word1Length){
            mergedString += word2.substring(i, word2Length); 
            return mergedString;
        // else return the string with no remainder appended
        } else {
            return mergedString;
        }
    } // end mergeAlternately()

    public static void main(String args[]) {
        MergeStringsAlternately merge = new MergeStringsAlternately();
        System.out.println("Expected: " + "apbqrs -- " + "Result: " +
                                merge.mergeAlternately("ab", "pqrs"));
        System.out.println("Expected: " + "apbqcr -- " + "Result: " +
                                merge.mergeAlternately("abc", "pqr"));
        System.out.println("Expected: " + "apbqcd -- " + "Result: " +
                                merge.mergeAlternately("abcd", "pq"));
    }
}


