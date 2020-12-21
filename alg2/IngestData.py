import csv

from alg2 import DeliveryStatus
from alg2.HashTable import HashTable
from alg2.truck import trucks

###TODO:  Confirm what time EOD actually is


EOD = "23:59:59"
with open('WGUPS_DISTANCE_FILE.csv') as input_file:
    distances = csv.reader(input_file, delimiter=',')
    distances = list(distances)
# Read in csv file that is the names of all possible delivery locations
with open('WGUPS_LOCATION_FILE.csv') as input_file:
    locations = csv.reader(input_file, delimiter=',')
    locations = list(locations)

with open('WGUPS_PACKAGE_FILE.csv') as input_file:
    slurpCSV = csv.reader(input_file, delimiter=",")
    working_hash_table = HashTable() #Make a new hashtable to work with

    #TODO:  Blow this up
    first_truck = []  # list that represents the first truck delivery
    second_truck = [] # list that represents the second truck delivery
    first_truck_second_trip = [] # list that represents the final truck delivery

    # for r in slurpCSV:
    #     r_package_ID = r[0]
    #     r_address = r[1]
    #     r_city = r[2]
    #     r_state = r[3]
    #     r_zip = r[4]
    #     r_deadline= r[5] #Deadline
    #     r_size = r[6]
    #     r_note = r[7]
    #    # r_value = [r_package_ID, "", r_address, r_city, r_state, r_zip, r_delivery, r_size, r_note, "", "At hub"]
    #     r_value = [r_package_ID, r_address, r_city, r_state, r_zip, r_deadline, r_size, r_note,'-1',DeliveryStatus.AT_HUB]
    #     key = r_package_ID
    #
    #     #TODO: Perform hard checks to clean up data before processing
    #     if r_value[6] != 'EOD':
    #         if 'None' in r_value[8] or 'Must' in r_value[8]:
    #             first_truck.append(r_value)  # this is a list that represents the first truck
    #             trucks[0].cargo.append(r_value) # this is a list that represents the first truck
    #     if 'Can only be' in r_value[8]:
    #         second_truck.append(r_value)
    #         trucks[1].cargo.append(r_value)
    #     if 'Delayed' in r_value[8]:
    #         second_truck.append(r_value)
    #         trucks[1].cargo.append(r_value)
    #     # change the wrong address package to the correct address
    #     if '84104' in r_value[5] and '10:30' not in r_value[6]:
    #         first_truck_second_trip.append(r_value)
    #         trucks[2].cargo.append(r_value)
    #     if 'Wrong address listed' in r_value[8]:
    #         r_value[2] = '410 S State St'
    #         r_value[5] = '84111'
    #         trucks[2].cargo.append(r_value)
    #         first_truck_second_trip.append(r_value)
    #     if r_value not in first_truck and r_value not in second_truck and r_value not in first_truck_second_trip:
    #         if len(second_truck) > len(first_truck_second_trip):
    #             first_truck_second_trip.append(r_value)
    #         else:
    #             second_truck.append(r_value)
    for row in slurpCSV:
        package_ID_row_value = row[0]
        address_row_value = row[1]
        city_row_value = row[2]
        state_row_value = row[3]
        zip_row_value = row[4]
        delivery_row_value = row[5]
        size_row_value = row[6]
        note_row_value = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'
        iterate_value = [package_ID_row_value, address_location, address_row_value, city_row_value, state_row_value,
                         zip_row_value, delivery_row_value, size_row_value, note_row_value, delivery_start,
                         delivery_status]

        key = package_ID_row_value
        value = iterate_value
        # In place constraints to create a list of packages that are loaded onto the trucks
        # The data structure here focuses on moving all attributes of a package into a nested listed.
        # This allows for quick lookup and sorting that can be based on every package detail
        # Below is the set of constraints that determine which packages are loaded in either of the two trucks
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_truck.append(value) # this is a list that represents the first truck
        if 'Can only be' in value[8]:
            second_truck.append(value)
        if 'Delayed' in value[8]:
            second_truck.append(value)
        # change the wrong address package to the correct address
        if '84104' in value[5] and '10:30' not in value[6]:
            first_truck_second_trip.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            first_truck_second_trip.append(value)
        if value not in first_truck and value not in second_truck and value not in first_truck_second_trip:
            if len(second_truck) > len(first_truck_second_trip):
                first_truck_second_trip.append(value)
            else:
                second_truck.append(value)
        working_hash_table.insert(key, value) # adds all values in csv file to to a hash table

    def get_hash_map():
        return working_hash_table

    # function used to grab the packages that are loaded into the first truck
    # Space-time complexity is O(1)
    def check_first_truck_first_trip():
        return first_truck

    # function used to grab the packages that are loaded into the second truck
    # Space-time complexity is O(1)
    def check_second_truck_first_trip():
        return second_truck

    # function used to grab the packages that are loaded into the first truck last
    # Space-time complexity is O(1)
    def check_first_truck_second_trip():
        return first_truck_second_trip
