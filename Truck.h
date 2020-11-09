#ifndef TRUCK_H
#define TRUCK_H
#include "csvstream.h"

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
			organize_data(row, count);
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
		else if (length == 9) {
			after[0] = temp[0];
			after[1] = temp[2];
			after[2] = temp[3];
			after[3] = temp[4];
			word = after;
		}
		else
			std::cout << "Syntax is incorrect, comma needs to be removed: " << word << std::endl;

		//std::cout << after << std::endl;
		delete[] temp;
		delete[] after;

		return std::stoi(word);
	}

	void build_load() {
		order_weights();

		if (trailer_length.compare(twenty_foot_container) == 0) {
			build_twenty_foot_container();
		}
		else if (trailer_length.compare(twenty_eight_truck) == 0) {
			build_twenty_eight_truck();
		}
		else if (trailer_length.compare(fourty_container) == 0) {
			build_fourty_container();
		}
		else if (trailer_length.compare(fourty_eight_trailer) == 0) {
			build_fourty_eight_trailer();
		}
		else if (trailer_length.compare(fourty_eight_trailer_dbl_stack) == 0) {
			build_fourty_eight_dbl_stack();
		}
		else if (trailer_length.compare(fifty_three_trailer) == 0) {
			build_fifty_three_trailer();
		}
		else if (trailer_length.compare(fifty_three_dbl_stack) == 0) {
			build_fifty_three_trailer_dbl_stack();
		}
		else if (trailer_length.compare(steel_flatbed) == 0) {
			build_steel_flatbed();
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

	void build_twenty_foot_container() {
		
	}

	void build_twenty_eight_truck() {

	}

	void build_fourty_container() {

	}

	void build_fourty_eight_trailer() {

	}

	void build_fourty_eight_dbl_stack() {

	}

	void build_fifty_three_trailer() {		
		
	}

	void build_fifty_three_trailer_dbl_stack() {

	}

	void build_steel_flatbed() {

	}

	//Matches IU to weight and then sorts the weights in ascending order.
	void order_weights() {
		std::map<std::string, std::map<std::string, std::string> >::iterator itr;
		std::map<std::string, std::string>::iterator ptr;
		int temp = 0;

		for (itr = iu_dim_weight.begin(); itr != iu_dim_weight.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				if (ptr->first.compare("4x4 Pallet") == 0)
					four_by_four++;

				else if (ptr->first.compare("4x6 Pallet Long") == 0)
					four_by_six++;

				else
					std::cout << "Add this size: " << ptr->first << std::endl;
			}
		}

		for (itr = iu_dim_weight.begin(); itr != iu_dim_weight.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				temp = string_to_int(ptr->second);
				pallets.push_back(std::make_pair(temp, itr->first));
			}
		}

		std::sort(pallets.begin(), pallets.end());

		for (long unsigned int i = 0; i < pallets.size(); i++) {
			std::cout << pallets[i].first << ": " << pallets[i].second << std::endl;
		}
		std::cout << "Pallet Count: " << pallets.size() << std::endl;

	}

	void print_load() {
		if (trailer_length.compare(twenty_foot_container) == 0) {


		}
		else if (trailer_length.compare(twenty_eight_truck) == 0) {

		}
		else if (trailer_length.compare(fourty_container) == 0) {

		}
		else if (trailer_length.compare(fourty_eight_trailer) == 0) {

		}
		else if (trailer_length.compare(fourty_eight_trailer_dbl_stack) == 0) {

		}
		else if (trailer_length.compare(fifty_three_trailer) == 0) {

		}
		else if (trailer_length.compare(fifty_three_dbl_stack) == 0) {

		}
		else if (trailer_length.compare(steel_flatbed) == 0) {

		}
		else {
			std::cout << "Error: Unrecognized Trailer... Unable to generate load." << std::endl;
		}

		/*std::map<bool, std::map<std::string, int> >::iterator itr;
		std::map<std::string, int>::iterator ptr;
		for (itr = pallet_positions.begin(); itr != pallet_positions.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				std::cout << "State: " << itr->first
					<< "   IU #: " << ptr->first
					<< "   Weight: " << ptr->second << std::endl;
			}
		}*/
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
	std::vector<std::pair<int, std::string>> pallets;
};

#endif