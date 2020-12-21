### Alexander Macey
### C950 Algorithms II

#IMPORTS
from alg2.IngestData import get_hash_map
from alg2.DeliveryStatus import *
from alg2.Distances import *
from alg2.Packages import total_distance

if __name__ == '__main__':

    commandList = '\tinsert - Create a new package.\n\tlook-up - Find a package at a given time.\n\ttime - find package states at a certain time.\n\tquit - End program.\n'
    command = "none"
    print('Route was completed in:', "{0:.2f}".format(total_distance(), 2), 'miles.')

    ###Convenience methods
    ##Gets an input string from user and makes it a a datetime
    def inputTime():
        (hours, minutes, seconds) = input('At what time?  HH:MM:SS:\n').split(':')
        return datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))


    ##Turns strings in our format into datetime objects
    def stringToDatetime(string):
        (h, m, s) = string.split(':')
        return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


    ##Console loop
    while command is not 'quit':
        if command == 'look-up':
            try:
                ##Get package_id and timestamp
                lookup_id = input('Please give package id:\n')
                any_given_time = inputTime()
                ###Print package data from Htable
                print('Package ID '+lookup_id + " at:", any_given_time)
                command = ""
                print('\n\tStreet address:',get_hash_map().get(str(lookup_id))[2], get_hash_map().get(str(lookup_id))[3],get_hash_map().get(str(lookup_id))[4], get_hash_map().get(str(lookup_id))[5],
                      '\n\tRequired delivery time:', get_hash_map().get(str(lookup_id))[6],
                      '\n\tPackage weight:', get_hash_map().get(str(lookup_id))[7],
                      '\n\tDeparture time:',get_hash_map().get(str(lookup_id))[9],
                      '\n\tDelivery time:',get_hash_map().get(str(lookup_id))[10])
            except ValueError:
                print("Input Error happened, try again.")
        elif command == 'time':
            try:
                #Get timestamp to check
                query_time = inputTime()
                # Space-time complexity is O(N^2)
                for packages_id in range(1, 41):
                    try:
                        departure_time = get_hash_map().get(str(packages_id))[9]
                        delivered_time = get_hash_map().get(str(packages_id))[10]
                    except ValueError:
                        print(ValueError)
                        pass
                    # First checks all packages against the given time determine if they have left the hub yet.
                    if stringToDatetime(departure_time) >= query_time:
                        get_hash_map().get(str(packages_id))[10] = AT_HUB
                        get_hash_map().get(str(packages_id))[9] = 'Leaves at ' + departure_time
                    elif stringToDatetime(departure_time) < query_time:
                        # Then checks to see which packages have left the hub but have not been delivered yet
                        if query_time < stringToDatetime(delivered_time):
                            get_hash_map().get(str(packages_id))[10] = 'In transit'
                            get_hash_map().get(str(packages_id))[9] = 'Left at ' + departure_time
                        else:
                            get_hash_map().get(str(packages_id))[10] = 'Delivered at ' + delivered_time
                            get_hash_map().get(str(packages_id))[9] = 'Left at ' + departure_time
                    print('Package ID:', get_hash_map().get(str(packages_id))[0], ", ", get_hash_map().get(str(packages_id))[9], ", ", get_hash_map().get(str(packages_id))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()
        elif command == 'insert':
            #Create a new package
            _package_id = input('package ID number:')
            _address = input('address:')
            _city = input('city:')
            _state = input('state:')
            _zip = input('zip:')
            _deadline = input('delivery deadline HH:MM:SS:')
            _weight = input('weight: ')
            _status = input('status (e.g., delivered, in route):')

            _value = [_package_id, "", _address, _city, _state, _zip, _deadline, _weight, "", "", _status]
            get_hash_map().insert(_package_id, _value)
            get_hash_map().print()

        elif command == 'quit':
            ##Quit
            exit()
        elif command == 'none':
            ##Do nothing
            print()
        else:
            print("Unknown command given.")
        command = input("Please input a command:\n" + commandList).lower()

