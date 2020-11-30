import csv
from alg2.HashTable import HashTable

with open('WGUInputData.csv') as csv:
    slurpCSV = csv.reader(csv, delimeter=",")
    working_hash_table = HashTable() #Make a new hashtable to work with
    truck_one = []
    truck_two = []
    truck_three = [] #Keep in mind this is actually the first truck, just making a second run

