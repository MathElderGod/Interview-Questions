# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

# Example 4:
# Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
# Output: [-6,2,4]
# Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 destroys -1. Since 2 and 4 are both moving right, they never collide.


# Constraints:
# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
def asteroidCollision(asteroids):
    stack = []
    # add the firs asteroid to the stack
    stack.append(asteroids[0])
    i = 1
    while i < len(asteroids):
        current_asteroid = asteroids[i]
        # case_1: current_asteroid and asteroid in the stack will collide (they have opposite signs)
        # specifically, current asteroid is heading left (neg), and stack is heading right (pos)
        # stack   | curr
        # ---------|------------
        # (+) --> | (+) -->
        # <-- (-) | <-- (-)
        # (+) --> | <-- (-)  ********* COLLISION!
        # <-- (-) | (+) -->
        if stack and ((current_asteroid < 0) and (stack[-1] > 0)):
            # sub_case1: current_asteroid blows up
            if abs(current_asteroid) < abs(stack[-1]):
                i += 1
            # sub_case2: stack asteroid blows up (update the stack)
            elif abs(current_asteroid) > abs(stack[-1]):
                stack.pop()
            # sub_case3: else they both blow up
            else:
                stack.pop()
                i += 1
        # case_2: current_asteroid and asteroid in the stack will NOT collide
        else:
            # simply append the current_asteroid to the stack
            stack.append(current_asteroid)
            i += 1
    # return the surviving asteroids
    return stack

test_cases = [
    [5, 10, -5],
    [8, -8],
    [10, 2, -5],
    [3, 5, -6, 2, -1, 4]
]

for asteroids in test_cases:
    result = asteroidCollision(asteroids)

    print("Input:  ", asteroids)
    print("Output: ", result, "\n")
