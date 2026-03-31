/** 
    For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

    Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

    Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

    Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

    Example 4:
    Input: str1 = "AAAAAB", str2 = "AAA"
    Output: ""​​​​​​​

    Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

*/

public class GcdOfStrings {
    public String gcdOfStrings(String str1, String str2) {
        // extract the length of both strings
        int str1Length = str1.length();
        int str2Length = str2.length();
        // if the string lengths are the same emter
        if (str1Length == str2Length) {
            // the strings are the same
            if (str1.equals(str2)){
                // return either or
                return str1;
                // else return the empty string
            } else {
                return "";
            }
        }

        // declare a gcd of strings
        String gcdOfStrings = "";
        // if string 1 is the smallest enter
        if (str1Length < str2Length) {
            // step 1: check if str2 matches the gcd
            // declare the current gcd
            String gcdString = "";
            // for every i-th character in string 1
            for(int i = 0; i < str1Length; i++){
                // declare a concatenation string
                String concatenatedString = "";
                // set the gcd to the current gcd string + ith character
                gcdString += str1.charAt(i);
                // concatenate the gcd string to itself upto (str2Length / (i + 1) times
                for(int j = 0; j < (str2Length / (i + 1)); j++){
                    concatenatedString += gcdString;
                }
                // get the length of the gcd string
                int gcdStringLength = gcdString.length();
                // if the concatenatedString is the same as string 2 and gcd divides both str1 and str2
                if (concatenatedString.equals(str2) && (str1Length % gcdStringLength == 0) && (str2Length % gcdStringLength == 0)) {
                    // set the gcd of strings to gcd string
                    gcdOfStrings = gcdString;
                }
            }

            // step 2: check if str1 matches the gcd
            // if the strings match, then return gcdOfStrings
            if (gcdOfStrings.equals(str1) || gcdOfStrings.equals("")) {
                return gcdOfStrings;
                // else the strings dont match, so we must check the concatenation
            } else {
                // get the length of the gcd of strings
                int gcdOfStringsLength = gcdOfStrings.length();
                // declare a concatenation string
                String concatenatedString = "";
                // concatenate the gcd of strings to itself upto  str1Length / gcdOfStringsLength
                for (int i = 0; i < str1Length / gcdOfStringsLength; i++) {
                    concatenatedString += gcdOfStrings;
                }
                // if the strings match, then return gcdOfStrings
                if (concatenatedString.equals(str1)) {
                    return gcdOfStrings;
                    // else return the empty string
                } else {
                    return "";
                }
            }
            // else string 2 is the smallest
        } else {
            // step 1: check if str1 matches the gcd
            // declare the current gcd
            String gcdString = "";
            // for every i-th character in string 2
            for(int i = 0; i < str2Length; i++) {
                // declare a concatenation string
                String concatenatedString = "";
                // set the gcd to the current gcd string + ith character
                gcdString += str2.charAt(i);
                // concatenate the gcd string to itself upto (str1Length / (i + 1) times
                for(int j = 0; j < (str1Length / (i + 1)); j++){
                    concatenatedString += gcdString;
                }
                // get the length of the gcd string
                int gcdStringLength = gcdString.length();
                // if the concatenatedString is the same as string 1 and gcd divides both str1 and str2
                if (concatenatedString.equals(str1) && (str1Length % gcdStringLength == 0) && (str2Length % gcdStringLength == 0)) {
                    // set the gcd of strings to gcd string
                    gcdOfStrings = gcdString;
                }
            }

            // step 2: check if str2 matches the gcd
            // if the strings match, then return gcdOfStrings
            if (gcdOfStrings.equals(str2) || gcdOfStrings.equals("")) {
                return gcdOfStrings;
                // else the strings dont match, so we must check the concatenation
            } else {
                // get the length of the gcd of strings
                int gcdOfStringsLength = gcdOfStrings.length();
                // declare a concatenation string
                String concatenatedString = "";
                // concatenate the gcd of strings to itself upto  str2Length / gcdOfStringsLength
                for (int i = 0; i < str2Length / gcdOfStringsLength; i++) {
                    concatenatedString += gcdOfStrings;
                }
                // if the strings match, then return gcdOfStrings
                if (concatenatedString.equals(str2)) {
                    return gcdOfStrings;
                    // else return the empty string
                } else {
                    return "";
                }
            }
        }
    }
    public static void main(String args[]){
        GcdOfStrings gcd = new GcdOfStrings();
        String str1 = "ABCABC";
        String str2 = "ABC";
        System.out.println("String 1: " + str1 + " String 2: " + str2);
        System.out.println("------------------------");
        System.out.println("Result: ABC " + "Expected: " +
        gcd.gcdOfStrings(str1, str2) + "\n");


        str1 = "ABABAB";
        str2 = "ABAB";
        System.out.println("String 1: " + str1 + " String 2: " + str2);
        System.out.println("------------------------");
        System.out.println("Result: AB " + "Expected: " + gcd.gcdOfStrings(str1,
        str2) + "\n");


        str1 = "ALEX";
        str2 = "ARIAS";
        System.out.println("String 1: " + str1 + " String 2: " + str2);
        System.out.println("------------------------");
        System.out.println("Result: '' " + "Expected: " + gcd.gcdOfStrings(str1,
        str2) + "\n");


        str1 = "AAAAAB";
        str2 = "AAA";
        System.out.println("String 1: " + str1 + " String 2: " + str2);
        System.out.println("------------------------");
        System.out.println("Result: '' " + "Expected: " + gcd.gcdOfStrings(str1,
        str2) + "\n");
    }
}
