#include <iostream>
#include <string>
#include <map>
#include "Matrix.h"

using namespace std;

void trailer_matrix(int width_in, int length_in) {
	
	
	if (length_in == 53 && width_in == 8.5) {

	}
	
	else if (length_in == 48 && width_in == 8) {

	}
	
	else if (length_in == 45 && width_in == 8) {

	}

	else if (length_in == 43 && width_in == 8){
	}
	
	else if (length_in == 28) {

	}

	else {
		cout << "Try a different length: " << std::endl;
	}

	
}

int main(int argc, char* argv[])
{
	multimap<string, int> pallet;
	trailer_matrix(stoi(argv[1]), stoi(argv[2]));
	

	return 0;
}

