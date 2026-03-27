/**
    Given an integer array nums, move all 0's to the end of it while maintaining 
    the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

 

    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Example 2:

    Input: nums = [0]
    Output: [0]
 

    Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
*/


import java.io.*;
import java.util.*;

class MoveZeroes {
    public void moveZeroes(int[] nums) {
        // if the length of nums is 1, return from the method
        int numsLength = nums.length;
        if(numsLength == 1) {
            return;
        }

        // initialize pointer i and j since nums length is greater than 1
        int i = 0;
        int j = 1;

        // iterate through nums
        while(i <= numsLength - 1) {
            // if i is 0 and j is not zero, swap the values
            if((j < numsLength) && (nums[i] == 0) && (nums[j] != 0)){
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                // increment i and set j to i + 1
                i++;
                j = i + 1;
            // else if i is 0 and j is 0, then increment j
            } else if((j < numsLength) && (nums[i] == 0) && (nums[j] == 0)) {
                j++;
            // else i is not 0, so we need to adjust the pointers accordingly
            } else {
                i++;
                j = i + 1;
            }
        }
    }

    public static void main(String args[]){
        MoveZeroes moveZeroes = new MoveZeroes();
        
        int numsArray1[] = {0, 1, 0, 3, 12};
        moveZeroes.moveZeroes(numsArray1);
        System.out.println("Expected: [1, 3, 12, 0, 0] " + " Result: " +
        Arrays.toString(numsArray1));

        int numsArray2[] = {0, 5, 0, 1, 0, 2, 15, 0, 0, 0, 5};
        moveZeroes.moveZeroes(numsArray2);
        System.out.println("Expected: [5, 1, 2, 15, 5, 0, 0, 0, 0, 0, 0] " + 
        " Result: " + Arrays.toString(numsArray2));

        int numsArray3[] = {0, 0};
        moveZeroes.moveZeroes(numsArray3);
        System.out.println("Expected: [0, 0] " + " Result: " + 
        Arrays.toString(numsArray3));

        int numsArray4[] = {1, 0};
        moveZeroes.moveZeroes(numsArray4);
        System.out.println("Expected: [1, 0] " + " Result: " + 
        Arrays.toString(numsArray4));

        int numsArray5[] = {0, 5};
        moveZeroes.moveZeroes(numsArray5);
        System.out.println("Expected: [5, 0] " + " Result: " + 
        Arrays.toString(numsArray5));

        int numsArray6[] = {10};
        moveZeroes.moveZeroes(numsArray6);
        System.out.println("Expected: [10] " + " Result: " + 
        Arrays.toString(numsArray6));
    }
}
