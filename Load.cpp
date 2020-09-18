#include <iostream>
#include <fstream>
#include <vector>
#include<iomanip>
#include <string>
#include <map>
#include <sstream>
#include "Matrix.h"

using namespace std;

/*




*/


void read_csv(string input) {
	string line, values, temp;
	vector<string> container;
	ifstream file_in;
	file_in.open(input);
	
	if (!file_in.is_open()) throw std::runtime_error("Could not open file");

	while (getline(file_in, temp, ',')) {
		if (temp.compare("") != 0) {
			cout << temp;
			container.push_back(temp);
		}
		
		
	}
	
	for (long unsigned int i = 0; i < container.size(); i++) {
		cout << container[i] << endl;
	}
	

	file_in.close();
}

int main(int argc, char* argv[])
{
	read_csv(argv[1]);
	
	return 0;
}

