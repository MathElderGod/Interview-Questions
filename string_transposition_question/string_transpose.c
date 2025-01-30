///////////////////////////////////////////////////////////////////////////////
/**
 *
 * Ah, I was asked this question during a coding assessment for EPIC Solutions
 * I wanted to tackle this problem again, because why not?
 *
 * Given a string consisting of unique characters, write a program that 
 * generates all possible transpositions of the string. A transposition 
 * is defined as swapping any two adjacent characters exactly once, and each 
 * unique swap should be included in the output.
 * 
 * For example, given the input "MUG", the valid transpositions would be:
 * 
 * Swapping 'M' and 'U' → "UMG"
 * Swapping 'U' and 'G' → "MGU"
 * Swapping 'M' and 'G' (skipping over 'U') → "GUM"
 * Swapping 'G' and 'U' (from "GUM") → "GMU"
 * 
 * The expected output for "MUG" would be:
 * {"UMG", "MGU", "GUM", "GMU"} 
 *
 * as it is supposed to show the process entirely. 
 *
 * Your task is to implement an efficient approach that takes any given string 
 * and returns all valid transpositions. You may assume that the input string 
 * contains only alphabetic characters and has a length of at least two.
 *
 * My Insights:
 *
 * Interesting findings! The total number of possible transpositions of a string  
 * of size n is (n - 1) ^ 2. Believe it or not, I realized this while eating
 * oatmeal cookies and drinking coke zero at 10:00pm ish...while testing out 
 * some strings.
 *
 * Give it a shot, by proving this yourself. I observed the pattern while testing 
 * out the words "COMPUTER", "TAKE", "ONOMATOPOEIA"..."FU", and ....well duh, a
 * string of size 1. lol
 *
 * Computer is a string of size 8, thus its total number of transpositions is 49.
 * 
 * Take has 9. 
 * 
 * and 
 *
 * Onomatopoeia has 121 transpositions. 
 *
 * Obviously, the solution is O(n^2) itself.
 * Also, the word will be spelt again vertically! MIND BLOWN!!!!
 *
 */

#include "string_transpose.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void){
	char someChar = '\0';
	// prompt the user to input another string, unless they type q for quit
	while(someChar != 'q'){
		// declare a new string 
	        char someString[MAX_BUFFER_SIZE];
		// prompt user
		printf("Enter a string, to see all possible string transpositions: ");
		int i;
		char currChar;
		// grab the string from stdin
		for(i = 0; (currChar = getchar()) != '\n'; i++){
			someString[i] = currChar;
		}
		// ensure the string ends with the sentinel
		someString[i] = '\0';
		// check if the string given is a valid single word string
		int validString = checkIfValidString(someString);
		// if not valid, make the user type in a correct word string
		if(!validString){
			printf("Error: String you entered was not valid. Make sure to enter a single word string!\n");
			continue;
		}
		// else the string is valid, thus find all transpositions of the string
		transposeString(someString);
		// ask the user if they'd like to continue
		printf("Try new string? Type anything that is not q if so. Else type q to quit program: ");
		// save their input to some char using scanf
		scanf("%c", &someChar);
		// clear the input buffer
		clearInputBuffer();
	}
	// transposition complete
	return EXIT_SUCCESS;
}

void clearInputBuffer(void){
	char c;
	while( ( (c = getchar()) != '\n')  && (c != EOF)){}
}

int checkIfValidString(char *someString){
	int stringLength = strlen(someString);
	// check every character
	for(int i = 0; i < stringLength; i++){
		// if the string has a space, it is more likely more than one word
		// in length
		if(*(someString + i) == ' '){
			// return not valid
			return 0;
		}
	}
	// return valid
	return 1;
}

void transposeString(char *someString){
	printf("---------String:\t%s\n", someString);
	int stringLength = strlen(someString);
	int transpositionCount = 0;
	for(int i = 0; i < stringLength - 1; i++){
		for(int j = 0; j < stringLength - 1; j++){
			// save the current char into temp
			char temp = someString[j];
			// swap the current char for next adjacent char
			someString[j] = someString[j + 1];
			// replace the adjacent char with the current char
			someString[j + 1] = temp;
			// increment the tranposition count
			transpositionCount++;
			// print the i-th transposed word
		        printf("Transposition %d:\t%s\n", transpositionCount, someString);
		}
	}
}

