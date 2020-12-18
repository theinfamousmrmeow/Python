### Alexander Macey

#IMPORTS

from alg2.HashTable import HashTable

from alg2.IngestData import get_hash_map

from alg2.DistanceData import *
from alg2.Distances import *
from alg2.Packages import total_distance

if __name__ == '__main__':

    #ht = HashTable()
    #ht.print()
    #ht.insert(0,"what a cat does")
    #ht.print()
    #get_hash_map().print()
    commandList = '\tinsert - Create a new package.\n\tlook-up - Find a package at a given time.\n\ttime - find package states at a certain time.\n\tquit - End program.\n'
    command = "none"
    get_hash_map().print()
    print('Current route was completed in', "{0:.2f}".format(total_distance(), 2), 'miles.')
   # first_time = get_hash_map().get(str("1"))[6]
   # print("FIRST_TIME")
   # print(first_time)

    ##Gets an input string from user and makes it a a datetime
    def inputTime():
        (hours, minutes, seconds) = input('At what time?  HH:MM:SS:\n').split(':')
        return datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

    while command is not 'quit':
        if command == 'look-up':
            try:
                ##Do lookup routine
                lookup_id = input('Please give package id:\n')
                ##Turn string into datetime
                any_given_time = inputTime()
                ###Print package data from Htable
                print('Package ID '+lookup_id + " at: ")
                print(any_given_time)
                print(get_hash_map().get(lookup_id))
                command = ""
            except ValueError:
                print("Input Error happened, try again.")
        elif command == 'timestamp':
            try:
                #package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                convert_user_time = inputTime()
                # Space-time complexity is O(N^2)
                for count in range(1, 41):
                    try:
                        print("Package ID :"+str(count))
                        get_hash_map().print()
                        first_time = get_hash_map().get(str(count))[9]
                        print(first_time)
                        second_time = get_hash_map().get(str(count))[10]
                        (h, m, s) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        print(ValueError)
                        pass
                    # First checks all packages against the given time determine if they have left the hub yet.
                    if convert_first_time >= convert_user_time:
                        get_hash_map().get(str(count))[10] = 'At Hub'
                        get_hash_map().get(str(count))[9] = 'Leaves at ' + first_time
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    elif convert_first_time <= convert_user_time:
                        # Then checks to see which packages have left the hub but have not been delivered yet
                        if convert_user_time < convert_second_time:
                            get_hash_map().get(str(count))[10] = 'In transit'
                            get_hash_map().get(str(count))[9] = 'Left at ' + first_time
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Required delivery time:', get_hash_map().get(str(count))[6],
                                  ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                                  get_hash_map().get(str(count))[9], '  Delivery status:',
                                  get_hash_map().get(str(count))[10])
                        # Finally checks all packages that have already been delivered and displays the delivered time
                        else:
                            get_hash_map().get(str(count))[10] = 'Delivered at ' + second_time
                            get_hash_map().get(str(count))[9] = 'Left at ' + first_time
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Required delivery time:', get_hash_map().get(str(count))[6],
                                  ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                                  get_hash_map().get(str(count))[9], '  Delivery status:',
                                  get_hash_map().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()
        elif command == 'insert':
            #Create a new package
            #r_value = [r_package_ID, "", r_address, r_city, r_state, r_zip, r_delivery, r_size, r_note, "", "At hub"]
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

