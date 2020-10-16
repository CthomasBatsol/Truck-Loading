#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include "bst.h"

std::vector<std::string> read_csv(std::string filename) {
	std::ifstream file;
	std::string word;
	std::vector<std::string> words;
	
	file.open(filename);
	if (!file.is_open()) throw std::runtime_error("Could not open file");

	while (getline(file, word,',')) {
		
		if(word.compare("") != 0) 
			words.push_back(word);
	}

	for (long unsigned int i = 0; i < words.size(); i++) {

		if (words[i].compare("53’ Trailer") == 0) {
			std::cout << "found -> " << i << ": " << words[i] << std::endl;
		}

		if (words[i].compare("48’ Trailer") == 0) {
			std::cout << "found -> " << i << ": " << words[i] << std::endl;
		}

		if (words[i].compare("40’ Trailer") == 0) {
			std::cout << "found -> " << i << ": " << words[i] << std::endl;
		}

		if (words[i].compare("28’ Trailer") == 0) {
			std::cout << "found -> " << i << ": " << words[i] << std::endl;
		}
	}

	return words;
}

void print_contents(std::vector<std::string> words) {
	
	for (long unsigned int i = 0; i < words.size(); i++) {
		std::cout << words[i] << std::endl;
	}

}

int main(int argc, char* argv[])
{
    std::vector<std::string> file_contents = read_csv(argv[1]);
	print_contents(file_contents);

	return 0;
}

