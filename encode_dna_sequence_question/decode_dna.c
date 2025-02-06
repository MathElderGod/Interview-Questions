///////////////////////////////////////////////////////////////////////////////
/**
 * This files sole purpose is to decode an encoded file, to check for correctness
 */
#include "decode_dna.h"
int main(int argc, char *argv[]){
	// check for correct number of command line args
        if(argc < 2){
                printf("Error: not enough command line arguements.\n");
                printf("Make sure to have ./decode_dna encoded_dna_file\n");
                return EXIT_FAILURE;
        }
        // attempt to open the file via read only
        FILE *infilePointer = fopen(argv[1], READ_ONLY);
        // if the file does not exist, exit the program
        if(infilePointer == NULL){
                printf("Error: The file: %s, you tried reading from does not exist!", argv[1]);
                return EXIT_FAILURE;
        }
	// decode the DNA Sequence
        decodeDNASequence(infilePointer);
	// close the file
        fclose(infilePointer);
	// exit the program successfully
        return EXIT_SUCCESS;
}

void decodeDNASequence(FILE *infilePointer){
	// open a new file to write to
        FILE *outfilePointer = fopen("decoded_dna_output", WRITE_ONLY);
	// set the current char and current number to the sentinel
        char currentCharacter = '\0';
	char currentNumber = '\0';
	// the character being read from the file
        int someCharacter;
	// to index my string number array
        int index = 0;
	// create a string number and empty number array
	char someNumber[MAX_BUFFER_SIZE];
	char emptyNumber[MAX_BUFFER_SIZE];
	// iterate through each character in the file
        while((someCharacter = getc(infilePointer)) != EOF){
		// if some char is not a number
		if( (someCharacter != ZERO) && (someCharacter != ONE) && (someCharacter != TWO)   && (someCharacter != THREE) &&
                                             (someCharacter != FOUR)  && (someCharacter != FIVE)  &&
                                             (someCharacter != SIX)   && (someCharacter != SEVEN) &&
                                             (someCharacter != EIGHT) && (someCharacter != NINE)){
			// if the current number is the sentinel
			if(currentNumber == '\0'){
				// set the current character to the new character being read
				currentCharacter = someCharacter;
				// write out the current character to the file
				putc(currentCharacter, outfilePointer);
			} else {
				// we must write out the number of times a certain character appears
				// end the number string with the sentinel
				someNumber[index] = '\0';
				// reset the index and the current number
				index = 0;
				currentNumber = '\0';
				// convert some number to an int
				int repeatCount = atoi(someNumber);
				// write out the character the times it repeats (not including its first instance)
				for(int i = 0; i < repeatCount; i++){
					putc(currentCharacter, outfilePointer);
				}
				// set the currentChar to the new character being read
				currentCharacter = someCharacter;
				// write out the currentChar to the file
				putc(currentCharacter, outfilePointer);
				// reset someNumber to an empty string
				strcpy(someNumber, emptyNumber);
			}
		// else its a number
		} else {
			// set the current index of somenumber to the current number being read
			someNumber[index] = (char) someCharacter;
			// set the current number to the number being read
			currentNumber = (char) someCharacter;
			// increment the index
			index++;
		}
	}
	// edge case
	// terminate some number with the sentinel
	someNumber[index] = '\0';
	// convert some number to an int
        int repeatCount = atoi(someNumber);
	// write out the character the times it repeats (not including its first instance)
        for(int i = 0; i < repeatCount; i++){
		putc(currentCharacter, outfilePointer);
        }
	// close the file
        fclose(outfilePointer);
}
