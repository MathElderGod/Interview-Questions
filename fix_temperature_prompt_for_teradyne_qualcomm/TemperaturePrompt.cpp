#include "TemperaturePrompt.hpp"

int main(void){
    string someTempString;
    vector<int> temps;
    // prompt user
    cout << "Please Enter a comma seperated value list of temperatures: ";
    getline(cin, someTempString);

    // keep prompting until valid
    while(!isValidTempString(someTempString)){
        // prompt the user for a valid temperature string again
        cout << "Please Try to enter a valid comma seperated value list of temperatures: ";
        getline(cin, someTempString);
    }

    // remove the white space in the string
    someTempString.erase(remove_if(someTempString.begin(), someTempString.end(), ::isspace), someTempString.end());
    // populate the temps array
    temps = populateTempsArray(someTempString);

    // if the temperatures were incorrect then we should quit, else proceed with testing
    if(!tempsInCSV("project_alpha.csv", temps)){
        cout << "The Information you entered is incorrect!\n";
        return EXIT_FAILURE;
    } else {
        cout << "Proceed with testing! :)\n";
        return EXIT_SUCCESS;
    }
}

/**
    A function that checks if the user provided valid temp string values are actually
    contained in a file of information for testing.
    @param filename a string filename of the file to open for reading
    @param someTempsArray an array of valid temperature values 
    @return true if the values are contained or false if they're not
*/
bool tempsInCSV(const string &filename, vector<int> someTempsArray){
    // create a copy of the vectors array into an unordered set
    unordered_set<int> setOfTemps(someTempsArray.begin(), someTempsArray.end());
    // open the file
    ifstream file(filename);
    // if the file is not open, return false. 
    if(!file.is_open()){
        cerr << "Failed to open file!.\n";
        return false;
    }
    string line;
    // skip the header
    getline(file, line);
    // get a line of information while the temps set is not empty
    while(getline(file, line) && !setOfTemps.empty()){
        // ss is a substring from the current line
        stringstream ss(line);
        // token is a value from the substring
        string token;
        // go to the temperature column
        for(int i = 0; i < 3; i++){
            getline(ss, token, ',');
        }
        // grab the temperature value from the temperature column
        getline(ss, token, ',');
        // turn the value into an integer from a string
        int temp = stoi(token);
        // if the value is in the unordered set, then remove it
        if(setOfTemps.find(temp) != setOfTemps.end()){
            setOfTemps.erase(temp);
        }
    }
    // if the set of temperatures is empty, then we can proceed with testing, else we cannot. 
    return setOfTemps.empty();
}

/**
    A function that populates a temps vector from the valid temperature string, and returns that vector
    @param somValidTempString a valid temperature string
    @return a vector of type int, consitisting of temperature values
*/
vector<int> populateTempsArray(string someValidTempString){
    const char *intVals = someValidTempString.c_str();
    char *endPtr;
    vector<int> temps;
    // keep adding temperatures until we reach the end of the string
    while(*(intVals) != '\0'){
        // get the first integer temperature
        int someTempVal = strtol(intVals, &endPtr, 10);
        // push it to the back of the vector
        temps.push_back(someTempVal);
        // if the endpointer is our comma delimeter, set the start pointer to the character that follows after
        if(*(endPtr) == ','){
            intVals = endPtr + 1;
        // else we can break out the loop for the last temperature
        } else {
            break;
        }
    }
    // return the vecotr array of temperatures
    return temps;
}

/**
    A function to print an array of temperatures. 
*/
void printTempsArray(vector<int> someTempArray){
    for(int someTemp : someTempArray){
        cout << someTemp << " ";
    }
}

/**
    A function that checks if a comma seperated list of temperature values is valid.
    @param someTempString a comma seperated list of temperature values
    @return true or false

*/
bool isValidTempString(string someTempString){
    // the string cant be empty
    if(someTempString.empty()){
        return false;
    }

    // currentCharPtr points to the current character in the string
    const char *currentCharPtr = someTempString.c_str();
    // grab the length of the string
    int tempStringSize = someTempString.length();
    
    // the string is size 1, simply check if its valid
    if(tempStringSize == 1){
        // check if its valid
        if(isValidVal(*(currentCharPtr))){
            return true;
        } else {
            return false;
        }
    }

    /***** string size is greater than 1 ****/
    // a string must start with a valid value or a -, else its garbage
    if((!isValidVal(*(currentCharPtr))) && (*(currentCharPtr) != '-')){
        return false;
    // a string cannot end with a comma
    } else if(someTempString.back() == ','){
        return false;
    }

    // nextCharPtr points to the next character from the current character
    const char *nextCharPtr = someTempString.c_str();
    nextCharPtr++;

    // if the next char pointer points to the end of a string, end the loop
    while(*(nextCharPtr) != '\0'){
        // if current char is a minus, then next char must be valid
        // if current char is a space, then next char must be minus (-) or valid
        // if current char is a comma, then next char must be space, minus (-), or valid, and not the end.
        // if current char is   valid, then next char must be valid or a comma. 
        if( (( *(currentCharPtr) == '-' )      && ( !isValidVal(*(nextCharPtr) ) )) ||
            (( *(currentCharPtr) == ' ' )      && ((*(nextCharPtr) != '-') && (!isValidVal(*(nextCharPtr))))) ||
            (( *(currentCharPtr) == ',' )      && ((*(nextCharPtr) != ' ') && (*(nextCharPtr) != '-') && (!isValidVal(*(nextCharPtr))))) ||
            (( (isValidVal(*(currentCharPtr))) && ((*(nextCharPtr) != ',') && (!isValidVal(*(nextCharPtr))))))){
            // the string is not valid, so return false.
            return false;
        }
        // update the ptr positions to point to the next characters
        currentCharPtr++;
        nextCharPtr++;
    } //O(n) runtime. 
    // the string is valid, so return true
    return true;
}

/**
    A function that checks a character to see if it's a number 
    @param someChar the character being checked
    @return true or false
*/
bool isValidVal(char someChar){
    switch(someChar){
        case '0':
            return true;
        case '1':
            return true;
        case '2':
            return true;
        case '3':
            return true;
        case '4':
            return true;
        case '5':
            return true;
        case '6':
            return true;
        case '7':
            return true;
        case '8':
            return true;
        case '9':
            return true;
        default:
            return false;
    }
}
