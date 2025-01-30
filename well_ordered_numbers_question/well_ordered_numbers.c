///////////////////////////////////////////////////////////////////////////////
/**
 *
 * I was asked this question while doing a coding assessment with EPIC solutions
 *
 * To be honest, I skipped this one because my brain couldn't comprehend at the time, 
 * that the problem was a combinatorics problem. 
 *
 * Jeez....all that studying in my discrete mathematics class really did not save 
 * me in the assessment. *SIGH* 
 *
 * By the way, why do they call discrete mathematics discrete, if there is nothing
 * discreet about it. (jajajaja ****laughs in spanish****) 
 *
 * **CRICKET NOISES**
 *
 * Anyways.....
 *
 * Interview Question:
 *
 * A well-ordered number is an integer whose digits are in strictly increasing order from left to right. This means that for any digit at position
 * i, it must be strictly less than the digit at position i + 1
 * For example:
 *
 * 149 is a well-ordered number because 1 < 4 < 9. 
 * 321 is not a well-ordered number because 3 !< 2 !< 1.
 *
 * Given an integer n, representing the number of digits in a well-ordered number, determine the total count of all possible well-ordered numbers of length n.
 * 
 * Constraints & Rules
 * The digits can only be chosen from {1,2,3,4,5,6,7,8,9}.
 * Each digit must be unique and in strictly increasing order.
 * An empty number (n = 0) is considered to have 1 valid arrangement (the empty set).
 *
 * A single-digit number (n = 1) has 9 valid arrangements: {1,2,3,4,5,6,7,8,9}.
 * If n > 9, output 0, since there aren't enough unique digits to form such a number.
 *
 * The order of digits must be preserved (e.g., "21" is not valid, but "12" is).
 * 
 * Example Cases
 * n	Output	Explanation
 * 0	1	Only the empty set is valid.
 * 1	9	{1,2,3,4,5,6,7,8,9}
 * 2	36	Pairs like {12, 13, ..., 89}.
 * 3	84	Triples like {123, 124, ..., 789}.
 * 4	126	Four-digit well-ordered numbers.
 * 9	1	Only {123456789} is possible.
 * 10	0	Impossible since there are only 9 unique digits.
 *
 * Follow-Up Questions
 *
 * Can you derive a formula to compute the result efficiently instead of generating all numbers?
 *	
 *	Answer: yes, by using the combination formula known as n!/(r!(n-r)!)....
 *
 * How would you approach solving this for large n in an optimal way?
 * 	
 * 	Answer: by simply having a base case that returns 0 for any n > 9
 *
 * Can you discuss the time complexity of your approach?
 * 	
 * 	Answer: The time complexity of my approach is O(1) since all of the arithmetic is done in constant
 * 		time, despite the recursion that was used. 
 */
#include "well_ordered_numbers.h"
#include <stdio.h>
#include <stdlib.h>
int main(void){
	char input = '\0';
	while(input != 'q'){
		// prompt the user to put in a size n of a number
		printf("Please enter the length of a number to find ALL possible well ordered numbers of a number of size n: ");
		int n;
		scanf("%d", &n);
		// consume any new line
		scanf("%*c");
		// check to see if the number n the user put in is valid
		if(n < 0){
			printf("Error: enter a valid integer size! \n");
			continue;
		}
		// find the number of well ordered numbers of a number of size n
		int numWellOrderedNumbers = findNumWellOrderedNumbers(n);
		printf("The number of well ordered numbers for a number of size n is: %d\n", numWellOrderedNumbers);
		// prompt the user to continue or not
		printf("Would you like to continue? Type q to quit, else type anything else: ");
		scanf("%c", &input);
		// consume any new line
		scanf("%*c");
	}
}

int findNumWellOrderedNumbers(int someSize){
	// if the n is 0, then the empty set is well ordered, thus return 1
	if(someSize == 0){
		return 1;
	// else if n is 9, then return 1
	} else if (someSize == MAX_DIGIT){
		return 1;
	// else if n is greater than 9, return 0
	} else if (someSize > MAX_DIGIT){
		return 0;
	} else {
		// else n is a valid size outside our base cases
	        // return 9!/(n!(9 - n)!) --> aka 9Cn
	        return (factorial(MAX_DIGIT) / (factorial(someSize) * factorial(MAX_DIGIT - someSize)));
	}
}

int factorial(int n){
	// base case, if n is 0, end the recursion by returning 1
	if(n == 0){
		return 1;
	}
	// recursive call to factorial, with n - 1 as its parameter
	return n * factorial(n - 1);
}
