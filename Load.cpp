#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include "csvstream.h"


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
/*
std::set<std::string> unique_words(const std::string& str) {
	std::istringstream source{ str };
	return{ std::istream_iterator<std::string>{source},
			std::istream_iterator<std::string>{} };
}*/

class truck {
public:
	truck() {
		debug_mode = false;
		gross_weight = 0;
		four_by_four = 0;
		four_by_six = 0;
	}

	truck(bool is_debug) {
		debug_mode = is_debug;
		gross_weight = 0;
		four_by_four = 0;
		four_by_six = 0;
	}

	void read_csv(std::string& argv) {
		int count = 0;
		csvstream c(argv);
		std::map<std::string, std::string> row;
		
		if (debug_mode) {
			std::cout << "Reading file... " << std::endl;
		}
		while (c >> row) {
			organize_data(row,count);
			count++;
		}
		
	}

	void organize_data(std::map<std::string, std::string>& row, int count) {
		std::map<std::string, std::map<std::string, std::string>>::iterator it;
		
		if (debug_mode) {
			if (count == 0) {
				trailer_length = row["TrailerTypeDisplay"];
				k_num = row["OrderID"];
				string_weight = row["cGrossWeight"];
				gross_weight = string_to_int(string_weight);
			}
			iu_dim_weight.insert(std::make_pair(row["InvUnit for OutShipment::InvUnitID"], std::map<std::string, std::string>()));
			iu_dim_weight[row["InvUnit for OutShipment::InvUnitID"]].insert(std::make_pair(row["UnitTypes for InvUnit for OutShipment::UnitType"], row["InvUnit for OutShipment::GrossWeight"]));
			iu_material_area.insert(std::make_pair(row["InvUnit for OutShipment::InvUnitID"], std::map<std::string, std::string>()));
			iu_material_area[row["InvUnit for OutShipment::InvUnitID"]].insert(std::make_pair(row["MRL for OutShipment InvUnit::MaterialName"], row["InvUnit for OutShipment::Area"]));

		}

	}

	int string_to_int(std::string word) {
		const char* weight = word.c_str();
		int length = strlen(weight);
		char* temp = new char[length];
		char* after = new char[length - 1];
		
		for (int i = 0; i < length; i++) {
			temp[i] = weight[i];
		}

		if (length == 7) {
			after[0] = temp[0];
			after[1] = temp[1];
			after[2] = temp[3];
			after[3] = temp[4];
			after[4] = temp[5];
			word = after;
		}
		else if (length == 6) {
			after[0] = temp[0];
			after[1] = temp[2];
			after[2] = temp[3];
			after[3] = temp[4];
			word = after;
		}
		else
			std::cout << "Weight is incorrect: " << word << std::endl;
		
		std::cout << after << std::endl;
		delete[] temp;
		delete[] after;

		return std::stoi(word);
	}

	void build_load() {
	

		if (trailer_length.compare(twenty_foot_container) == 0) {
			build_twenty_foot_container(iu_dim_weight,iu_material_area);
		}
		else if (trailer_length.compare(twenty_eight_truck) == 0) {
			build_twenty_eight_truck(iu_dim_weight);
		}
		else if (trailer_length.compare(fourty_container) == 0) {
			build_fourty_container(iu_dim_weight);
		}
		else if (trailer_length.compare(fourty_eight_trailer) == 0) {
			build_fourty_eight_trailer(iu_dim_weight);
		}
		else if (trailer_length.compare(fourty_eight_trailer_dbl_stack) == 0) {
			build_fourty_eight_dbl_stack(iu_dim_weight);
		}
		else if (trailer_length.compare(fifty_three_trailer) == 0) {
			build_fifty_three_trailer(iu_dim_weight,iu_material_area);
		}
		else if (trailer_length.compare(fifty_three_dbl_stack) == 0) {
			build_fifty_three_trailer_dbl_stack(iu_dim_weight);
		}
		else if (trailer_length.compare(steel_flatbed) == 0) {
			build_steel_flatbed(iu_dim_weight);
		}
		else {
			std::cout << "Error: Unrecognized Trailer... Unable to generate load." << std::endl;
		}
	}

	//Considerations:
	//1. What are the dimensions? 4x4-> 1 space. 4x6-> 2 spaces.
	//2. Can it be double stacked? -> type of material.
	//3. Split load evenly, 25% of load in each quadrant.
	//4. Heaviest materials in the middle. 

	void build_twenty_foot_container(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight_in, std::map<std::string, std::map<std::string, std::string>> iu_material_area_in) {
		std::map<std::string, std::map<std::string, std::string> >::iterator itr;
		std::map<std::string, std::string>::iterator ptr;
		
		for (itr = iu_dim_weight.begin(); itr != iu_dim_weight.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				if (ptr->first.compare("4x4 Pallet") == 0) {
					
				}
			}
		}
	}

	void build_twenty_eight_truck(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight) {
		
	}

	void build_fourty_container(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight) {
		
	}

	void build_fourty_eight_trailer(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight) {
		
	}

	void build_fourty_eight_dbl_stack(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight) {
		
	}

	void build_fifty_three_trailer(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight, std::map<std::string, std::map<std::string, std::string>> iu_material_area_in) {
		std::map<std::string, std::map<std::string, std::string> >::iterator itr;
		std::map<std::string, std::string>::iterator ptr;

		for (itr = iu_dim_weight.begin(); itr != iu_dim_weight.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				if (ptr->first.compare("4x4 Pallet") == 0 )
					four_by_four++;

				else if (ptr->first.compare("4x6 Pallet Long") == 0)
					four_by_six++;

				else
					std::cout << "Add this size: " << ptr->first << std::endl;
			}
		}
		


	}

	void build_fifty_three_trailer_dbl_stack(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight) {
		
	}

	void build_steel_flatbed(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight) {
		
	}

	void order_weights(std::map<std::string, std::map<std::string, std::string>> iu_dim_weight_in) {
		std::map<std::string, std::map<std::string, std::string> >::iterator itr;
		std::map<std::string, std::string>::iterator ptr;

		for (itr = iu_dim_weight.begin(); itr != iu_dim_weight.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {

			}
		}

	}

	void print_load() {
		std::map<std::string, std::map<std::string, std::string> >::iterator itr;
		std::map<std::string, std::string>::iterator ptr;
		for (itr = iu_material_area.begin(); itr != iu_material_area.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				std::cout << "IU #: " << itr->first
					<< "   Material: " << ptr->first
					<< "   Area: " << ptr->second << std::endl;
			}
		}
	}



private:
	bool debug_mode;
	int four_by_four;
	int four_by_six;
	int gross_weight;
	std::string string_weight;
	std::string trailer_length;
	std::string k_num;
	std::string twenty_foot_container = "20’ Container";
	std::string twenty_eight_truck = "28’ Truck";
	std::string fourty_container = "40’ Container";
	std::string fourty_eight_trailer = "48’ Trailer";
	std::string fourty_eight_trailer_dbl_stack = "48’ Trailer Dbl Stack";
	std::string fifty_three_trailer = "53’ Trailer";
	std::string fifty_three_dbl_stack = "53’ Dbl Stack";
	std::string steel_flatbed = "Steel Flatbed";
	std::map<std::string, std::map<std::string, std::string>> iu_dim_weight;
	std::map<std::string, std::map<std::string, std::string>> iu_material_area;
	std::map<bool, std::map<std::string, int>> pallet_positions;
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
		load.build_load();
		
	}

	catch (csvstream_exception& csv) {
		std::cout << csv.msg << std::endl;
	}

	return 0;
}

