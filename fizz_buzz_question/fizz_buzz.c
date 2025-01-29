///////////////////////////////////////////////////////////////////////////////
/**
 * Ah! The infamous fizz-buzz question....
 *
 * Write a program that prints numbers from 1 to a specified number, 
 * replacing any multiple of 3 with "Fizz", any multiple of 5 with 
 * "Buzz", and any multiple of both 3 and 5 with "FizzBuzz"
 * */

#include "fizz_buzz.h"
#include <stdio.h>
#include <stdlib.h>
int main(void){
	char someChar = '\0';
	// some number n, that the user will enter
	int n;
	// prompt the user to enter a number, until they quit the program
	while(someChar != 'q'){
		printf("Enter a number: ");
		scanf("%d", &n);
		// consume any remaining new line
		scanf("%*c");
		// print the fizz-buzz pattern for numbers 1 through n
		fizzBuzz(n);
		// ask the user if they'd like to continue
		printf("Continue? type q to quit, else type any other char: ");
		scanf("%c", &someChar);
		// consume any remaining new line
		scanf("%*c");
	}
	// program termination successful
	return EXIT_SUCCESS;
}
void fizzBuzz(int someNumber){
	// for numbers 1 upto some specified number
	for(int i = 1; i <= someNumber; i++){
		// if divisible by 3 and 5, print FizzBuzz
		if((i % THREE == 0) && (i % FIVE == 0)){
			printf("%s\n", FIZZ_BUZZ);
		// else if divisible by three only print Fizz
		} else if(i % THREE == 0){
			printf("%s\n", FIZZ);
		// else if divisible by five only print Buzz
		} else if(i % FIVE == 0){
			printf("%s\n", BUZZ);
		// else not dividible, so simply print the number i
		} else {
			printf("%d\n", i);
		}
	}
}
