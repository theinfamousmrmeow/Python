import csv
from alg2.HashTable import HashTable

with open('WGUPS_PACKAGE_FILE.csv') as input_file:
    slurpCSV = csv.reader(input_file, delimiter=",")
    working_hash_table = HashTable() #Make a new hashtable to work with
    truck_one = []
    truck_two = []
    truck_three = [] #Keep in mind this is actually the first truck, just making a second run

    for r in slurpCSV:
        r_package_ID=r[0]
        r_address = r[1]
        r_city = r[2]
        r_state = r[3]
        r_zip = r[4]
        r_delivery = r[5]
        r_size = r[6]
        r_note = r[7]
        r_value = [r_package_ID, "", r_address, r_city, r_state, r_zip, r_delivery, r_size, r_note, "", "At hub"]
        key = r_package_ID

        #TODO: Perform hard checks to clean up data before processing

        working_hash_table.insert(key,r_value)

    def get_hash_map():
        return working_hash_table