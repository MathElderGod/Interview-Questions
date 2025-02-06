///////////////////////////////////////////////////////////////////////////////
/**
 *
 * I was asked this interview question by A big FAANG company.
 * they usually grow on orchards! ;}. 
 *
 * Why am I tackling this problem again? because I want to prove
 * to myself that my encoding solution works. I was the one that came
 * up with it anyway. I also want to practice more. 
 *
 * Coding Interview Question: DNA Sequence Encoding
 * Problem Statement:
 * You are given a text file containing a DNA sequence consisting of the characters 
 * A, T, C, and G. Your task is to write a program that reads the DNA sequence from 
 * the file and encodes it using a modified run-length encoding scheme. 
 * The encoded DNA sequence should then be written to a separate output file.
 * Encoding Rules:
 * The first occurrence of a nucleotide is written as-is.
 * If the nucleotide repeats consecutively, it is followed by the count of additional occurrences.
 * Single occurrences of a nucleotide are written as-is without a number.
 * Example:
 *
 * Input File (dna_input.txt)
 * GGGGGTTCAATC
 * Output File (dna_encoded.txt)
 * G4T1CA1C
 *
 * Explanation:
 * GGGGG → G4 (1 G followed by 4 more Gs)
 * TT → T1 (1 T followed by 1 more T)
 * C → C (appears once, so remains unchanged)
 * AA → A1 (1 A followed by 1 more A)
 * T → T (appears once, so remains unchanged)
 * C → C (appears once, so remains unchanged)
 * */

#include "encode_dna.h"
int main(int argc, char *argv[]){
	// check for correct number of command line args
	if(argc < 2){
		printf("Error: not enough command line arguements.\n");
		printf("Make sure to have ./encode_dna dna_sequence_file\n");
		return EXIT_FAILURE;
	}
	// attempt to open the file via read only
	FILE *infilePointer = fopen(argv[1], READ_ONLY);
	// if the file does not exist, exit the program
	if(infilePointer == NULL){
		printf("Error: The file: %s, you tried reading from does not exist!", argv[1]);
		return EXIT_FAILURE;
	}
	// encode the DNA Sequence
	encodeDNASequence(infilePointer);
	// close the file
	fclose(infilePointer);
	// exit the program successfully
	return EXIT_SUCCESS;
}

void encodeDNASequence(FILE *infilePointer){
	// open a new file for writing out to
	FILE *outfilePointer = fopen("encoded_dna_output", WRITE_ONLY);
	int someCharacter;
        char currentCharacter = '\0';
        int count = 0;
	// as long as we have not reached the EOF, we will iterate through each character
        while((someCharacter = getc(infilePointer)) != EOF){
		// if the current character has changed
                if(currentCharacter != (char) someCharacter){
			// check to see if the count is greater than 0
                        if(count > 0){
				// write the number of times a character appeared after
				// its first appeareance to the file
				fprintf(outfilePointer, "%d", count);
                        }
			// reinitialize the current character to the new character
                        currentCharacter = (char) someCharacter;
			// write the new character to the file
			putc(currentCharacter, outfilePointer);
			// reset the count
                        count = 0;
                } else {
			// else the number repeats, so increment the count
                        count++;
                }
        }

	// edge case, if DNA sequence ends on a repeated character, we need to write out the final count
	if(count > 0){
		// write the number of times a character appeared after
                // its first appeareance to the file
		fprintf(outfilePointer, "%d", count);
	}
	// close the file
	fclose(outfilePointer);
}
