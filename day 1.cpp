#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include<algorithm> 
#include<stdlib.h>
#include <cstddef>
#include <regex>
using namespace std;
bool find_string(string line) {
	if (line.find("one") != string::npos) {return 1;}
	if (line.find("two") != string::npos) {return 1;}
	if (line.find("three") != string::npos) {return 1;}
	if (line.find("four") != string::npos) {return 1;}
	if (line.find("five") != string::npos) {return 1;}
	if (line.find("six") != string::npos) {return 1;}
	if (line.find("seven") != string::npos) {return 1;}
	if (line.find("eight") != string::npos) {return 1;}
	if (line.find("nine") != string::npos) {return 1;}
	return 0;
}
string str_to_char(string line) {
	line = regex_replace(line, regex("one"), "1");
	line = regex_replace(line, regex("two"), "2");
	line = regex_replace(line, regex("three"), "3");
	line = regex_replace(line, regex("four"), "4");
	line = regex_replace(line, regex("five"), "5");
	line = regex_replace(line, regex("six"), "6");
	line = regex_replace(line, regex("seven"), "7");
	line = regex_replace(line, regex("eight"), "8");
	line = regex_replace(line, regex("nine"), "9");
	return line;
}
int main() {
	int total = 0;
	string input;
	string line;
	char delim = '\n';
	//char letter;
	ifstream f("day1.txt"); //taking file as inputstream
   	if(f) {
      	ostringstream ss;
      	ss << f.rdbuf(); // reading data
     	input = ss.str();
   	}
	size_t pos = 0;
	while ((pos = input.find(delim)) != string::npos) {
		line = input.substr(0,pos);
		cout << line << endl;

		int i,j = 0;
		char first = '0'; 
		char last = '0';
		string line_past = "";
		for(char& letter : line) {
			if (isdigit(letter)){
				first = char(letter);
				break;
			} else {
				line_past += letter;
				//cout << line_past << endl;
				if (find_string(line_past)){
					line_past = str_to_char(line_past);
					//cout << line_past << endl;
					for(char& temp : line_past){
						if (isdigit(temp)) {
							first = char(temp);
							//cout << "found a number " << first << endl;
							break;
						}
					}
					break;
				}
			}
			i++;
		}
		line_past = "";
		reverse(line.begin(), line.end());
		for(char& letter :  line) {
			if (isdigit(letter)){
				last = char(letter);
				break;
			} else {
				line_past += letter;
				reverse(line_past.begin(), line_past.end());
				if (find_string(line_past)){
					line_past = str_to_char(line_past);
					for(char& temp : line_past){
						if (isdigit(temp)){
							last = char(temp);
							break;
						} else {
							reverse(line_past.begin(), line_past.end());
						}
					}
					break;
				} else {
					reverse(line_past.begin(), line_past.end());
				}
				
			}
			j++;
		} 
		string t;
		t += first;
		t += last;
		cout << t << endl;

		int line_total = stoi(t);
		total += line_total;

		input.erase(0, pos + 1);

	}

	cout << total << endl;
	// first correct total is 54159
 	return 0;
}
