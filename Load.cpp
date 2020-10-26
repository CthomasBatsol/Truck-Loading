#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include "csvstream.h"
#include "bst.h"


/* IMPORTANT: Input file must be in .csv format or else the program will not run	*/
/* IMPORTANT: Make sure you have saved the file in the same directory as the script */
/* Step 1: Look up the desired shipment in FileMaker								*/
/* Step 2: Click the "File" tab														*/
/* Step 3: Hover over "Save/Send Records As"										*/
/* Step 4: Click on "Excel"															*/
/* Step 5: Save the record as the order number 										*/
/* Step 6: Open the file you just saved and save it again as a .csv file			*/
/* Step 7: Run ./Load.exe K###### in the command prompt								*/
/* Step 8: Load the truck according to the diagram on the output					*/		


std::set<std::string> unique_words(const std::string& str) {
	std::istringstream source{ str };
	return{ std::istream_iterator<std::string>{source},
			std::istream_iterator<std::string>{} };
}

class truck {
public:
	truck() {
		debug_mode = false;
	}

	truck(bool is_debug) {
		debug_mode = is_debug;

	}

	void read_csv(std::string& argv) {
		csvstream c(argv);
		std::map<std::string, std::string> row;
		
		if (debug_mode) {
			std::cout << "Reading file... " << std::endl;
		}
		while (c >> row) {
			organize_data(row);
		}
		
	}

	void organize_data(std::map<std::string, std::string>& row) {
		std::set<std::string> trailer, weight, dimensions, i_u_num, area;
		std::map<std::string, std::string>::iterator it_1, it_2, it_3, it_4, it_5;

		it_1 = row.find("TrailerTypeDisplay");
		it_2 = row.find("InvUnit for OutShipment::GrossWeight");
		it_3 = row.find("UnitTypes for InvUnit for OutShipment::UnitType");
		it_4 = row.find("InvUnit for OutShipment::InvUnitID");
		it_5 = row.find("InvUnit for OutShipment::Area");

		trailer = unique_words(row.find("TrailerTypeDisplay")->second);
		weight = unique_words(row.find("InvUnit for OutShipment::GrossWeight")->second);
		dimensions = unique_words(row.find("UnitTypes for InvUnit for OutShipment::UnitType")->second);
		i_u_num = unique_words(row.find("InvUnit for OutShipment::InvUnitID")->second);
		area = unique_words(row.find("InvUnit for OutShipment::Area")->second);
		
		if (debug_mode) {
			std::cout << " IU = " << row["InvUnit for OutShipment::InvUnitID"] << "	" << "Dimensions = " << row["UnitTypes for InvUnit for OutShipment::UnitType"] << "	  " <<" Weight = " << 
				row["InvUnit for OutShipment::GrossWeight"] <<"	"<<"Location = " << row["InvUnit for OutShipment::Area"] << std::endl;
		}

	}

	//IDEA: Use the maps generated in organize_data() to properly build the load. 
	//This is where the BST will come into play.
	void build_load() {


	}


private:
	bool debug_mode;
	std::map<std::string, std::string> i_u_to_location;
	std::map < std::string, std::map<std::string, std::string>> i_u_to_weight_to_dims;
};

//Come back to this later...******************************************************************
bool input_check(int argc, char* argv[], bool& is_debug) {
	if (argc != 1 && argc != 2) {
		std::cout << "Usage: load.exe INCORRECT AMOUNT OF INPUTS [--debug]" << std::endl;
		return false;
	}
	else
	{
		if (argc == 2) {
			is_debug = true;
			return true;
		}
		else
		{
			if (!strcmp(argv[1], "--debug")) {
				is_debug = true;
				return true;
			}
			else {
				std::cout << "Usage: load.exe INCORRECT SPELLING [--debug]" << std::endl;
				return false;
			}
		}
	}
}
//**********************************************************************************************


int main(int argc, char* argv[])
{
	bool is_debug = false;
	if (!input_check(argc, argv, is_debug)) 
		return -1;
	std::string file = argv[1];
	truck load(is_debug);
	
	try {
		load.read_csv(file);
		
	}

	catch (csvstream_exception& csv) {
		std::cout << csv.msg << std::endl;
	}

	return 0;
}

