////////////////////////////////////////////////////////////////////////////////
/**
  * I was asked this question when I was doing a coding assessment with EPIC  
  * solutions.
  * 
  * Interview Question:
  *
  * Given that an ancient civilization used to use number encoded messages as their 
  * communication method, write a program that can decode their language.
  * 
  * let 
  * '*': " " (space)
  * '#': ""  (end of letter)
  *  0 : "0"
  *  1 : "1"
  *  2 : "ABC2"
  *  3 : "DEF3"
  *  4 : "GHI4"
  *  5 : "JKL5"
  *  6 : "MNO6"
  *  7 : "PQRS7"
  *  8 : "TUV8"
  *  9 : "WXYZ9"
  * 
  * Encoded Message: 44#444#*#8#44#33#777#33#
  * Decoded Message: HI THERE
  *
  * condition: excess instances cause circular behavior: ie. 44444# will be 'G'
  *
  * 2#555#33#99#2#66#3#33#777#*#4#*#2#777#444#2#7777#*#2222#4444#6666#2222# prints out ALEXANDER G ARIAS 2462
  *	
  *	input: 
  *
  *	      *#**##
  *	      0#00##
  *	      1#11##
  *	      2#22##222###2222####22222
  *	######3#33###333####3333#####33333
  *	######4#44###444####4444#####44444
  *	######5#55###555####5555#####55555
  *	######6#66###666####6666#####66666
  *	######7#77###777####7777#####77777#######777777
  *	######8#88###888####8888#####88888
  *	######9#99###999####9999#####99999#######999999#
  *	
  *	ouput: 0011ABC2ADEF3DGHI4GJKL5JMNO6MPQRS7PTUV8TWXYZ9W
  *
  */
#include "decoder.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void){
	char decision = '\0';
	char someLetter = '\0';
	char *decodedMessage;
	// prompt the user to decode a message until they choose not to. 
	while(decision != 'q'){
	        // clear the message at the start
		char someMessage[MAX_BUFFER_SIZE];
		// prompt the user
		printf(PROMPT);
		int i;
		// get the message from stdin using getchar()
		for(i = 0; (someLetter = getchar()) != '\n'; i++){
			someMessage[i] = someLetter;
		}
		// ensure to end the string with the sentinel
		someMessage[i] = '\0';
		// save the message length
		int someMessageLength = strlen(someMessage);
		// check the strings validity
		int messageIsValid = checkValid(someMessage, someMessageLength);
		// if the message is invalid, continue back to the top and prompt the user again
		if(!messageIsValid){
			printf("Error: The string you entered is not in the correct format. Try again!\n");
			// clear the input buffer
			// clearInputBuffer();
			continue;
		}
		// show the user the message they put
		printf("The message you entered was: %s\n", someMessage);
		// decode the message the user gave
		decodedMessage = decodeMessage(someMessage, someMessageLength);
		// sanity check, decoded message will be NULL if mem allo failed or if wrong formatted string
		// ie: not in the form of 44#33#*#4
		if(decodedMessage == NULL){
			printf("Error: Failed to allocate memory, or wrong string format! Try again.\n");
			return EXIT_FAILURE;
		}
		// show the user the decoded message 
		printf("The decoded Message is: %s\n", decodedMessage);
		// free the memory we allocated
		free(decodedMessage);
		// set the decoded message to NULL
		decodedMessage = NULL;
		// prompt the user if theyd like to continue
		printf(CONTINUE_MESSAGE);
		scanf("%c", &decision);
		// clear the input buffer
		clearInputBuffer();
	}
	return EXIT_SUCCESS;
}

void clearInputBuffer(void){
	int c;
	while( ((c = getchar()) != '\n') && (c != EOF) ){}
}

int checkValid(char *someMessage, int someMessageLength){
	char *currCharPtr = NULL;
	char *nextCharPtr = NULL;
	// check the message for validity
	for(int i = 0; i < someMessageLength; i++){
		currCharPtr = someMessage + i;
		nextCharPtr = someMessage + i + 1;
		// if the message consists of continguous different chars with no END_OF_LETTER in between pairs, then it is not correct.
		if((*currCharPtr != END_OF_LETTER) && (*nextCharPtr != END_OF_LETTER)
				&& (*currCharPtr != *nextCharPtr)){
			// message is invalid
			return 0;
		}
	}
	// message is valid
	return 1;
}

char* decodeMessage(char *someMessage, int someMessageLength){
	char decodedLetter = '\0';
	char* currCharPtr = NULL;
	char* nextCharPtr = NULL;
	char* decodedMessage = malloc(someMessageLength * sizeof(char) + 1);
	// if failed to allocate memory, return NULL
	if(decodedMessage == NULL){
		printf("Error: failed to allocate memory!\n");
		return NULL;
	}
	int count = 0;
	int j = 0;
	// check each char instance
	for(int i = 0; i < someMessageLength; i++){
		// char pointers will be used to check chars against each other
		currCharPtr = someMessage + i;
		nextCharPtr = someMessage + i + 1;
		// if the chars are the same, increment the count
		if(*currCharPtr == *nextCharPtr){
			count++;
			continue;
		}
		// if the char is the end of a letter, reset the count, and skip it
		if(*currCharPtr == END_OF_LETTER){
			count = 0;
			continue;
		}
		// decode the letter by calling decode letter given an input and the amount of times
		// it appeared
		decodedLetter = decodeLetter(*currCharPtr, count);
		// if somehow the letter is not recognized, then return NULL
		if(decodedLetter == '\0'){
			return NULL;
		}
		// append the decoded letter to our string
		decodedMessage[j] = decodedLetter;
		// reset the count
		count = 0;
		// increment our string position for the decoded message
		j++;
	}
	decodedMessage[j] = '\0';
	// the message was decoded correctly
	return decodedMessage;
}

char decodeLetter(char currentChar, int count){
	// set ptr size to 1.
	// to avoid division by zero, which causes floating point exception
	int ptrSize = 1;
	// switch case, skipping the # char, since it is simply the end of the letter
	// uses count modulo ptrsize, to pinpoint the correct position of the desired char
	switch(currentChar){
		case '*':
			ptrSize = strlen(SPACE_ACTUAL);
			return *(SPACE_ACTUAL + (count % ptrSize));
		case '0':
			ptrSize = strlen(ZERO_STRING);
			return *(ZERO_STRING + (count % ptrSize));
		case '1':
			ptrSize = strlen(ONE_STRING);
			return *(ONE_STRING + (count % ptrSize));
		case '2':
			ptrSize = strlen(TWO_STRING);
			return *(TWO_STRING + (count % ptrSize));
		case '3':
			ptrSize = strlen(THREE_STRING);
			return *(THREE_STRING + (count % ptrSize));
		case '4':
			ptrSize = strlen(FOUR_STRING);
			return *(FOUR_STRING + (count % ptrSize));
		case '5':
			ptrSize = strlen(FIVE_STRING);
			return *(FIVE_STRING + (count % ptrSize));
		case '6':
			ptrSize = strlen(SIX_STRING);
			return *(SIX_STRING + (count % ptrSize));
		case '7':
			ptrSize = strlen(SEVEN_STRING);
			return *(SEVEN_STRING + (count % ptrSize));
		case '8':
			ptrSize = strlen(EIGHT_STRING);
			return *(EIGHT_STRING + (count % ptrSize));
		case '9':
			ptrSize = strlen(NINE_STRING);
			return *(NINE_STRING + (count % ptrSize));
		default:
			printf("Unrecognized Char: %c\n", currentChar);
			return '\0';
	}
}
