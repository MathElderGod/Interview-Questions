# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 
# Constraints:
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

import math
def canPlaceFlowers(flowerbed, n):
    # get the flower bed length
    flowerbed_length = len(flowerbed)
    # determine the maximum number of flowers that can be planted in a flower bed
    max_flowers = math.ceil(flowerbed_length / 2)
    # get the number of flowers to plant
    flowers_to_plant = n
    # set a count for the number of flowers in the flower bed
    current_num_flowers = 0
    # get the count of flowers in the flower bed
    for i in range(flowerbed_length):
        if flowerbed[i] == 1:
            current_num_flowers += 1
    # get the total number of flowers expected in the flower bed
    total_flowers = current_num_flowers + flowers_to_plant
    # base case, if there are too many flowers to plant return false
    if total_flowers > max_flowers:
        return False
    # base case, you can always plant 0 flowers
    elif n == 0:
        return True
    # base case, we have enough flowers to plant and flowerbed consists of one plot
    elif flowerbed_length == 1 and n <= max_flowers:
        return not flowerbed[0]
    # other cases for a flowerbed with more than 1 plot, and with enough flowers to plant
    else:
        # make a copy of the flowerbed
        current_flowerbed = flowerbed
        # set a counter for the current flower plot
        i = 0
        # as long as we remain inside the flowerbed, enter
        while i < flowerbed_length:
            # if there are no more flowers to plant, break out the loop
            if flowers_to_plant == 0:
                break
            # Case 1: we are at the start, and both the current and next flower plots are empty
            first_plot_case = (i == 0) and (current_flowerbed[i] == current_flowerbed[i + 1]) and (current_flowerbed[i] == 0)
            # Case 2: we are anywhere else between the beginning and the end of the flower bed, and the previous-current-next flower plots are empty
            middle_plot_case = (0 < i < (flowerbed_length - 1)) and (current_flowerbed[i] == current_flowerbed[i - 1]) and (current_flowerbed[i] == current_flowerbed[i + 1]) and (current_flowerbed[i] == 0)
            # Case 3: we are at the end, and both the current and previous flower plots are empty
            last_plot_case = (i == flowerbed_length - 1) and (current_flowerbed[i] == current_flowerbed[i - 1]) and (current_flowerbed[i] == 0)
            # if any of the above cases is true, then enter
            if first_plot_case or middle_plot_case or last_plot_case:
                # flower the current flower plot
                current_flowerbed[i] = 1
                # decrement flowers to plant
                flowers_to_plant -= 1
                # skip over 2 plots of the flower bed
                i += 2
            # else it is the case that the current flower plot already has a flower,
            # or there are flowers in both the previous and/or next flower plots and the current plot cannot be flowered as a result
            else:
                # skip over 1 plot of the flower bed
                i += 1
        # return true if there are no more flowers to plant, else returns false
        return not flowers_to_plant

flowerbed = [1,0,0,0,1]
n = 1
print("Flowerbed:         ", flowerbed, " Flowers to plant = ", n)
print("Can be planted: ", canPlaceFlowers(flowerbed, n), " Expected: True\n")

flowerbed = [1,0,0,0,1]
n = 2
print("Flowerbed:         ", flowerbed, " Flowers to plant = ", n)
print("Can be planted: ", canPlaceFlowers(flowerbed, n), " Expected: False\n")

flowerbed = [0, 1, 0]
n = 1
print("Flowerbed:         ", flowerbed, " Flowers to plant = ", n)
print("Can be planted: ", canPlaceFlowers(flowerbed, n), " Expected: False\n")

flowerbed = [0,1,0,1,0,1,0,0]
n = 1
print("Flowerbed:         ", flowerbed, " Flowers to plant = ", n)
print("Can be planted: ", canPlaceFlowers(flowerbed, n), " Expected: True\n")

flowerbed = [0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]
n = 17
print("Flowerbed:         ", flowerbed, " Flowers to plant = ", n)
print("Can be planted: ", canPlaceFlowers(flowerbed, n), " Expected False")
