#define SPACE '*'
char* const SPACE_ACTUAL = " ";
#define END_OF_LETTER '#'
char* const END_ACTUAL = "";
char* const ZERO_STRING = "0";
char* const ONE_STRING = "1";
char* const TWO_STRING = "ABC2";
char* const THREE_STRING = "DEF3";
char* const FOUR_STRING = "GHI4";
char* const FIVE_STRING = "JKL5";
char* const SIX_STRING = "MNO6";
char* const SEVEN_STRING = "PQRS7";
char* const EIGHT_STRING = "TUV8";
char* const NINE_STRING = "WXYZ9";
#define MAX_BUFFER_SIZE 512
#define PROMPT "Given the following ancient language decoding pattern such that:\n\tInput     :     Result\n\t-----------------------------------------------\n\t*         :     ' ' (space)\n\t#         :     ''  (end of letter)\n\t0         :     0\n\t1         :     1\n\t2         :     ABC2\n\t3         :     DEF3\n\t4         :     GHI4\n\t5         :     JKL5\n\t6         :     MNO6\n\t7         :     PQRS7\n\t8         :     TUV8\n\t9         :     WXYZ9\n\tExample: the message: '44#444#*#8#44#33#777#33#' translates to 'HI THERE'\nPlease enter a correctly formatted message to decode: "
#define CONTINUE_MESSAGE "Would you like to decode another message? (type 'q' to quit, else type a different char to continue): "
void clearInputBuffer(void);
int checkValid(char *someMessage, int messageSize);
char* decodeMessage(char *someMessage, int messageSize);
char decodeLetter(char someChar, int count);
