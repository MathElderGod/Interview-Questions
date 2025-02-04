///////////////////////////////////////////////////////////////////////////////
/**
 * 
 *
 * I was asked this coding question by EPIC solutions.
 * Now, at the time, I realize I did a terrible job implementing the solution under 
 * the stress of the assessment timer. 
 *
 * Why don't companies just give you a programming assignment, and just have you turn
 * it in by a much broader and leniant deadline? A man can dream.....(AI ofcourse is 
 * the reason why.)
 *
 * Anyways, here we go.
 *
 * Interview Question:
 *
 * You are part of a lottery verification team. So far, there are two seperate lottery events  
 * going on at the same time. Each event has participants put down their phone numbers on a list. 
 * Particpants are only allowed to put down one phoner number, and are no longer allowed to 
 * participate in any other events for the lottery as a whole. Some particpants however, decided to 
 * violate the rules, and they have put down their phone numbers in the other list as well. 
 * Write a program that saves each users phone numbers, sorts them, and removes any cheaters from the 
 * overall lottery population. Return a SORTED list such that it is a list fully comprising of
 * the phone numbers of individuals that did not cheat.
 *
 * GAURANTEE: PHONE NUMBERS WILL NOT START WITH 0. Only one number can appear on one list. Since signing
 * up is proctored. This means that a particpant is forced to leave once they sign up their number. 
 * This means there can only be 1 duplicate instance of a number on a sperate list. 
 */

#include "remove_cheaters.h"
#include <stdlib.h>
int main(int argc, char **argv){
	// if the user does not provide exactly 3 arguements
	if(argc != THREE){
		// inform the user of the error
		printf("Error: You must provide exactly 3 command line arguements!\n");
		printf("Make sure you run the program as: ./program file1 file2\n");
		// exit program
		return EXIT_FAILURE;
	}

	// point to the files the user mentioned in the command line args
	FILE *infilePointer1 = fopen(argv[1], READ_ONLY);
	FILE *infilePointer2 = fopen(argv[TWO], READ_ONLY);
	// if any of the files the user provided do not exist
	if((infilePointer1 == NULL) || (infilePointer2 == NULL)){
		// inform the user the file(s) does/do not exist
		printf("Error: the file %s or %s that you tried to open does not exist! Try again.\n", argv[1], argv[TWO]);
		// try to close any files that exist
		if(infilePointer1 != NULL){
			fclose(infilePointer1);
		}
		if(infilePointer2 != NULL){
			fclose(infilePointer2);
		}
		// exit program
		return EXIT_FAILURE;
	}

	// Files have been successfully opened
	// Now it is time to read through each file
	int numCount = 0;
	// set an empty list
	unsigned long long combinedListOfNumbers[MAX_BUFFER_SIZE];
	// zero it out
	initializeArrayToZero(combinedListOfNumbers, MAX_BUFFER_SIZE);
	// add all phone numbers to the list from files 1 and 2
	numCount = appendPhoneNumbers(combinedListOfNumbers, numCount, infilePointer1);
	numCount = appendPhoneNumbers(combinedListOfNumbers, numCount, infilePointer2);
	// make a new list
	unsigned long long combinedList[numCount];
	// zero it out
	initializeArrayToZero(combinedList, numCount);
	// copy the exact numbers down
	copyArray(combinedList, combinedListOfNumbers, numCount);
	// sort the combined list, including the duplicates
	qsort(combinedList, numCount, sizeof(unsigned long long), compare);
	// print out the none cheaters
	printNoneCheaters(combinedList, numCount);
	// close the files that have been opened, before exiting program
	fclose(infilePointer1);
	fclose(infilePointer2);
	return EXIT_SUCCESS;
}

void initializeArrayToZero(unsigned long long *someArray, int size){
	// set index i to zero of some array of ints
	for(int i = 0; i < size; i++){
		someArray[i] = 0;
	}
}

int appendPhoneNumbers(unsigned long long arrayOfNumbers[], int numCount, FILE *someFilePtr){
	int someChar;
        int i = 0;
        char someNumber[] = NUMBER_FORMAT;
        // Go through each number on the file
        while((someChar = getc(someFilePtr)) != EOF){
                // if someChar is the new line, then we must add the number to our list of combined numbers
                if(someChar == '\n'){
                        // reinitialize the ith position
                        i = 0;
                        // set the numCount position at the combined list to the integer representation of someNumber
                        arrayOfNumbers[numCount] = strtoull(someNumber, NULL, 10);
                        // increment the num count
                        numCount++;
                // else if someChar is the -, simply skip that character
                } else if(someChar == '-'){
                        // continue to the next position
                        continue;
                // else overwrite the number
                } else {
                        // set the position at i to some char
                        someNumber[i] = someChar;
                        // increment the position i
                        i++;
                }
        }
	// return the total count of numbers that have been appended so far.
	return numCount;
}

void copyArray(unsigned long long someArray[], unsigned long long someOtherArray[], int numCount){
	// copy someOtherArray into someArray
	for(int i = 0; i < numCount; i++){
		someArray[i] = someOtherArray[i];
	}
}

// Comparison function
int compare(const void* a, const void* b) {
    unsigned long long num1 = *(unsigned long long*)a;
    unsigned long long num2 = *(unsigned long long*)b;

    if (num1 < num2) return -1;
    if (num1 > num2) return 1;
    return 0;
}

void printNoneCheaters(unsigned long long combinedList[], int numCount){
	printf("The participants that followed the rules are as follows: \n");
	// for each number, only print out the formatted non-cheating numbers. 
        for(int i = 0; i < numCount; i++){
                char phoneNumber[] = "XXX-XXX-XXXX";
                if(numCount == 1){
                        formatNumber(combinedList[i], phoneNumber);
                } else if((i == numCount - 1) && (combinedList[i] != combinedList[i - 1])){
                        formatNumber(combinedList[i], phoneNumber);
                } else if(combinedList[i] != combinedList[i + 1]){
                        formatNumber(combinedList[i], phoneNumber);
                } else {
                        // skip two spaces to skip the cheater
                        i += 1;
                }
        }
}

void formatNumber(unsigned long long someNumber, char *numberToFormat){
	// temp for number conversion
	char temp[PHONE_NUMBER_SIZE + 1];
	// format the number
	snprintf(temp, sizeof(temp), "%llu", someNumber);
	numberToFormat[0] = temp[0];
	numberToFormat[1] = temp[1];
	numberToFormat[TWO] = temp[TWO];
	// skip i = 3
	numberToFormat[FOUR] = temp[THREE];
	numberToFormat[FIVE] = temp[FOUR];
	numberToFormat[SIX] = temp[FIVE];
	// skip i = 7
	numberToFormat[EIGHT] = temp[SIX];
	numberToFormat[NINE] = temp[SEVEN];
	numberToFormat[TEN] = temp[EIGHT];
	numberToFormat[ELEVEN] = temp[NINE];
	// print out the formatted number
	printf("%s\n", numberToFormat);
}

