/**
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true
    
    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false
    
    Constraints:
    1 <= flowerbed.length <= 2 x 10^4
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
 */

import java.lang.Math;
class CanPlaceFlowers {
    /**
        This function determines whether flowers can be planted, without violating the contraints set by the problem
        @param flowerbed an array representing the current flowerbed consisting of 0's and 1's. (0 means empty) and (1 means flowered)
        @return true or false
    */
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        // get the flower bed length
        int flowerBedLength = flowerbed.length;
        // determine the maximum number of flowers that can be planted in a flower bed
        int maxFlowers = (int)(Math.ceil((double) flowerBedLength / 2));
        // get the number of flowers to plant
        int flowersToPlant = n;
        // set a count for the total number of flowers
        int currentNumFlowers = 0;
        // set a count for the total number of flowers currently in the flower bed
        for (int i = 0; i < flowerBedLength; i++) {
            if (flowerbed[i] == 1) {
                currentNumFlowers++;
            }
        }
        // get the total number of flowers expected in the flower bed
        int totalFlowers = currentNumFlowers + flowersToPlant;
        // base case, if too many flowers will be planted, return false
        if (totalFlowers > maxFlowers) {
            return false;
            // else if the flowers to plant is 0, you can always plant 0 flowers
        } else if (flowersToPlant == 0) {
            return true;
            // else if there is exactly one plot...
        } else if ((flowerBedLength == 1) && (flowersToPlant <= maxFlowers)) {
            if (flowerbed[0] == 0) {
                return true;
            } else {
                return false;
            }
            // else there are more than one flower plot
        } else {
            // create a shallow copy of the flowerbed
            int currentFlowerBed[] = flowerbed.clone();
            // set a counter for the current flower plot
            int i = 0;
            // as long as we remain in the flower bed, enter
            while (i < flowerBedLength) {
                // if there are no more flowers to plant, break out the loop
                if (flowersToPlant == 0) {
                    break;
                }
                // Case 1: we are at the start, and both the current and next flower plots are empty
                boolean firstPlotCase = (i == 0) && (currentFlowerBed[i] == currentFlowerBed[i + 1]) && (currentFlowerBed[i] == 0);
                // Case 2: we are anywhere else between the beginning and the end of the flower bed, and the 
                // previous-current-next flower plots are empty
                boolean middlePlotCase = (i > 0) && (i < (flowerBedLength - 1)) && (currentFlowerBed[i] == currentFlowerBed[i - 1]) && (currentFlowerBed[i] == currentFlowerBed[i + 1]) && (currentFlowerBed[i] == 0);
                // Case 3: we are at the end, and both the current and previous flower plots are empty
                boolean lastPlotCase = (i == flowerBedLength - 1) && (currentFlowerBed[i] == currentFlowerBed[i - 1]) && (currentFlowerBed[i] == 0);
                // set canPlantFlower to true if any of the cases above are true, else false
                boolean canPlantFlower = firstPlotCase || middlePlotCase || lastPlotCase;
                // if we can plant a flower, then plant it in the current flower plot
                if (canPlantFlower) {
                    currentFlowerBed[i] = 1;
                    flowersToPlant--;
                    i += 2;
                    // else skip over to the next flower plot
                } else {
                    i++;
                }
            }
        }
        // return true if there are no more flowers to plant, else false
        if (flowersToPlant == 0) {
            return true;
        } else {
            return false;
        }
    }

    /**
        This function prints the flowerBed, unmodified.
    */
    public void printFlowerBed(int[] flowerBed){
        System.out.print("[");
        int flowerBedLength = flowerBed.length;
        for(int i = 0; i < flowerBedLength; i++) {
            if(i == flowerBedLength - 1) {
                System.out.print(flowerBed[i]);
            } else {
                System.out.print(flowerBed[i] + ", ");
            }
       }
       System.out.println("]");
    }

    public static void main(String args[]){
        int flowerbed1[] = {1, 0, 0, 0, 1};
        int n = 1;
        CanPlaceFlowers canPlaceFlowers = new CanPlaceFlowers();
        canPlaceFlowers.printFlowerBed(flowerbed1);
        System.out.print("Can Place " + n + " Flowers? --> ");
        System.out.println(canPlaceFlowers.canPlaceFlowers(flowerbed1, n) + "\n");
        
        n = 2;
        canPlaceFlowers.printFlowerBed(flowerbed1);
        System.out.print("Can Place " + n + " Flowers? --> ");
        System.out.println(canPlaceFlowers.canPlaceFlowers(flowerbed1, n));

    }
}
