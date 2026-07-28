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
    # if the total number of flowers exceeds max flowers return false
    if total_flowers > max_flowers:
        return False
    # base case of n == 0
    elif n == 0:
        return True
    # base case of flower bed length == 1
    elif flowerbed_length == 1 and n <= max_flowers:
        return not flowerbed[0]
    # other cases for flower bed length >= 2
    else:
        # make a copy of the flowerbed
        current_flowerbed = flowerbed
        # set a counter for the current flower section
        i = 0
        # as long as we remain inside the flowerbed, enter
        while i < flowerbed_length:
            # if there are flowers to plant, and we are at the start, and both the current and next flower sections are empty, then enter
            if (flowers_to_plant != 0) and (i == 0) and (current_flowerbed[i] == current_flowerbed[i + 1]) and (current_flowerbed[i] == 0):
                # update the current flowerbed
                current_flowerbed[i] = 1
                # decrement flowers to plant
                flowers_to_plant -= 1
                # skip over 2 sections of the flower bed
                i += 2
            # else if there are flowers to plant, and we are at the end, and both the current and previous flower sections are empty, then enter
            elif (flowers_to_plant != 0) and (i == flowerbed_length - 1) and (current_flowerbed[i] == current_flowerbed[i - 1]) and (current_flowerbed[i] == 0):
                # update the current flowerbed
                current_flowerbed[i] = 1
                # decrement flowers to plant
                flowers_to_plant -= 1
                # skip over 2 sections of the flower bed
                i += 2
            # else if there are flowers to plant, we are anywhere else between the beginning and end of the flower bed, and the previous-current-next 
            # flower sections are empty, then enter
            elif (flowers_to_plant != 0) and (i > 0) and (i < flowerbed_length - 1) and (current_flowerbed[i] == current_flowerbed[i - 1]) and (current_flowerbed[i] == current_flowerbed[i + 1]) and (current_flowerbed[i] == 0):
                # update the current flowerbed
                current_flowerbed[i] = 1
                # decrement flowers to plant
                flowers_to_plant -= 1
                # skip over 2 sections of the flower bed
                i += 2
            # else it is the case that the current flower section has a flower planted already, and cannot be planted or 
            # there are flowers both in the previous and/or next flower sections and the current section cannot be planted
            else:
                # skip over 1 section of the flower bed
                i += 1
        #print("Updated Flowerbed: ", current_flowerbed)
        #print("Flowers left to plant: ", flowers_to_plant)
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
