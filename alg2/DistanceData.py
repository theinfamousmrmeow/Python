import csv
import datetime
from alg2.truck import truck, TRUCK_SPEED

# Read the map of distances between locations
with open('WGUPS_DISTANCE_FILE.csv') as input_file:
    distance_list = csv.reader(input_file, delimiter=',')
    distance_list = list(distance_list)
    #(distance_list)

# Read the csv of address locations
with open('WGUPS_LOCATION_FILE.csv') as input_file:
    location_list = csv.reader(input_file, delimiter=',')
    location_list = list(location_list)
    #print(location_list)

    #Computes distance from point A to point B
    def point_distance(a, b):
        d = distance_list[a][b]
        #Try it transposed if we can't find it
        if d is '':
            d = distance_list[b][a]
        return d