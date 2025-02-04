#define TWO 2
#define THREE 3
#define FOUR 4
#define FIVE 5
#define SIX 6
#define SEVEN 7
#define EIGHT 8
#define NINE 9
#define TEN 10
#define ELEVEN 11
#define TWELVE 12
#define NUMBER_FORMAT "0000000000"
#define MAX_BUFFER_SIZE 256
#define READ_ONLY "r"
#define PHONE_NUMBER_SIZE 10
#include <stdio.h>
void initializeArrayToZero(unsigned long long *someArray, int size);
int appendPhoneNumbers(unsigned long long *arrayOfNumbers, int numCount, FILE *someFilePtr);
void copyArray(unsigned long long *someArray, unsigned long long *someOtherArray, int numCount);
int compare(const void* a, const void* b);
void printNoneCheaters(unsigned long long combinedList[], int numCount);
void formatNumber(unsigned long long someNumber, char *numberToFormat);
