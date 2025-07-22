#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <vector>
using namespace std;

bool tempsInCSV(const string &filename, vector<int> someTempsArray);
vector<int> populateTempsArray(string someValidTempString);
void printTempsArray(vector<int> someTempsArray);
bool isValidTempString(string someTempString);
bool isValidVal(char someChar);

