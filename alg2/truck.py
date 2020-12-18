###Trucks don't do much, except have a cargo list that tells me which packages are on which truck
###I think it is fun to have more object-oriented algorithms, I come from an OOP background so these things make more sense to me.


NUM_TRUCKS = 3##Number of trucks that exist in the universe
NUM_DRIVERS = 2##So we can only have two trucks out at a time...
TRUCK_SPEED = 18
TRUCK_CAPACITY = 16

class truck:
    cargo = []
    departure_time = -1
    return_time = -1
    id = -1

##Just used for loading really
trucks=[truck(),truck(),truck()]

trucks_on_road=0 #Used to keep track of how many trucks are being driven right now