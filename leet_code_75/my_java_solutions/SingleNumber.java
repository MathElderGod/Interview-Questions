/**
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Example 1:
    Input: nums = [2,2,1]
    Output: 1

    Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

    Example 3:
    Input: nums = [1]
    Output: 1
    
    Constraints:
    1 <= nums.length <= 3 x 104
    -3 x 104 <= nums[i] <= 3 x 104
    Each element in the array appears twice except for one element which appears only once.
*/

class SingleNumber {
    /**
        This function takes in a list of numbers, and returns the unique number
        contained within the list, assuming that all elements, but one, repeat 
        no more than twice. One of the elements must occure once.
        @param nums a list of integers with one unique number
        @return uniqueNumber an int representing the unique number in nums
    */
    public int singleNumber(int[] nums) {
        // set a variable for the unique number
        int uniqueNumber = 0;
        // get the size of nums
        int numsLength = nums.length;
        // XOR each element in the array together
        for(int i = 0; i < numsLength; i++) {
            uniqueNumber = uniqueNumber ^ nums[i];
        }
        // return the unique number based on the XOR property
        return uniqueNumber;
    }
    /**
        This function prints a given list nums.
        @param nums a list of numbers
        @return none
    */
    public void printNums(int[] nums){
        System.out.print("[");
        int numsLength = nums.length;
        for(int i = 0; i < numsLength; i++) {
            if(i == numsLength - 1) {
                System.out.print(nums[i]);
            } else {
                System.out.print(nums[i] + ", ");
            }
       }
       System.out.println("]");
    }

    public static void main(String agrs[]) {
        // Test Case 1:
        int nums1[] = {2, 2, 1};
        SingleNumber singleNumber = new SingleNumber();
        singleNumber.printNums(nums1);
        System.out.println("Unique Number: " + singleNumber.singleNumber(nums1) + "\n");
        
        // Test Case 2:
        int nums2[] = {4, 1, 2, 1, 2};
        singleNumber.printNums(nums2);
        System.out.println("Unique Number: " + singleNumber.singleNumber(nums2) + "\n");
        
        // Test Case 3:
        int nums3[] = {1};
        singleNumber.printNums(nums3);
        System.out.println("Unique Number: " + singleNumber.singleNumber(nums3));
    }
}
