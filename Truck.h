#ifndef TRUCK_H
#define TRUCK_H
#include <iostream>
#include <fstream>
#include "csvstream.h"


class truck {
public:
	truck() {
		debug_mode = false;
		gross_weight = 0;
	}

	truck(bool is_debug) {
		debug_mode = is_debug;
		gross_weight = 0;
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

		delete[] temp;
		delete[] after;

		return std::stoi(word);
	}

	void build_load(std::string& output) {
		order_weights();

		if (trailer_length.compare(twenty_foot_container) == 0) {
			build_twenty_foot_container(output);
		}
		else if (trailer_length.compare(twenty_eight_truck) == 0) {
			build_twenty_eight_truck(output);
		}
		else if (trailer_length.compare(fourty_container) == 0) {
			build_fourty_container(output);
		}
		else if (trailer_length.compare(fourty_eight_trailer) == 0) {
			build_fourty_eight_trailer(output);
		}
		else if (trailer_length.compare(fourty_eight_trailer_dbl_stack) == 0) {
			build_fourty_eight_dbl_stack(output);
		}
		else if (trailer_length.compare(fifty_three_trailer) == 0) {
			build_fifty_three_trailer(output);
		}
		else if (trailer_length.compare(fifty_three_dbl_stack) == 0) {
			build_fifty_three_trailer_dbl_stack(output);
		}
		else if (trailer_length.compare(steel_flatbed) == 0) {
			build_steel_flatbed(output);
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

	void build_twenty_foot_container(std::string& output_in) {

	}

	void build_twenty_eight_truck(std::string& output_in) {

	}

	void build_fourty_container(std::string& output_in) {

	}

	void build_fourty_eight_trailer(std::string& output_in) {

	}

	void build_fourty_eight_dbl_stack(std::string& output_in) {

	}

	void build_fifty_three_trailer(std::string& output_in) {
		std::map<std::string, std::map<std::string, std::string>>::iterator itr;
		std::map<std::string, std::string>::iterator ptr;
		std::ofstream file;
		int count = 0;
		int four_by_six_count = 0;
		file.open(output_in);
		file << "CAB" << "," << "CAB" << std::endl;

		//Heaviest pallets to go in spots 7:18
		//Lightest pallets to go in spots 1:6-19:24
		for (itr = iu_dim_weight.begin(); itr != iu_dim_weight.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				
				if (ptr->first.compare("4x4 Pallet") == 0 && count == 0) {
					file << itr->first << ",";
					count++;
				}

				else if (ptr->first.compare("4x4 Pallet") == 0 && count == 1) {
					file << itr->first << "," << std::endl;
					count = 0;
					std::cout << count << std::endl;
				}

				else if (ptr->first.compare("4x6 Pallet Long") == 0) {
					count = 0;
					if (four_by_six_count == 0) {
						file << std::endl << itr->first << "," << "4x6" << std::endl;
						four_by_six_count++;
					}
					else {
						file << itr->first << "," << "4x6" << std::endl;
						four_by_six_count++;
					}

				}

				else {
					std::cout << "Add this size: " << ptr->first << std::endl;
				}
			}
		}

		file << "DOCK" << "," << "DOCK";
		file.close();
	}

	void build_fifty_three_trailer_dbl_stack(std::string& output_in) {

	}

	void build_steel_flatbed(std::string& output_in) {

	}

	//Matches IU to weight and then sorts the weights in ascending order.
	void order_weights() {
		std::map<std::string, std::map<std::string, std::string> >::iterator itr;
		std::map<std::string, std::string>::iterator ptr;
		int temp = 0;

		for (itr = iu_dim_weight.begin(); itr != iu_dim_weight.end(); itr++) {
			for (ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
				temp = string_to_int(ptr->second);
				pallets.push_back(std::make_pair(temp, itr->first));
			}
		}

		std::sort(pallets.begin(), pallets.end());
	}

private:
	bool debug_mode;
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