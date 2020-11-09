#include <iostream>
#include "csvstream.h"
#include "Truck.h"


/* IMPORTANT: Input file must be in .csv format or else the program will not run	*/
/* IMPORTANT: Make sure you have saved the file in the same directory as the script */
/* Step 1: Look up the desired shipment in FileMaker								*/
/* Step 2: Click the "File" tab														*/
/* Step 3: Hover over "Save/Send Records As"										*/
/* Step 4: Click on "Excel"															*/
/* Step 5: Save the record as the order number 										*/
/* Step 6: Open the file you just saved and save it again as a .csv file			*/
/* Step 7: Run ./Load.exe K###### in the command prompt								*/
/* Step 8: Load the truck according to the diagram in the output					*/		



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
		load.build_load();
		
	}

	catch (csvstream_exception& csv) {
		std::cout << csv.msg << std::endl;
	}

	return 0;
}

