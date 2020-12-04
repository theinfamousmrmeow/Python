### Alexander Macey

#IMPORTS

from alg2.HashTable import HashTable
from alg2.IngestData import get_hash_map

if __name__ == '__main__':

    ht = HashTable()
    ht.print()
    ht.insert(0,"what a cat does")
    ht.print()
    get_hash_map().print()
    commandList = '\tfind - Find a package at a given time.\n\ttime - find package states at a certain time.\n\tquit - End program.\n'
    command = "none"

    while command is not 'quit':
        if command == 'find':
            try:
                ##Do lookup routine
                lookup_id = input('Please give package id:\n')
                lookup_time = input('At what time?  HH:MM:SS:\n')
                ###Print package data from Htable
                command = ""
            except ValueError:
                print("Error happened, try again.")
        elif command == 'quit':
            ##Quit
            exit()
        elif command == 'none':
            ##Do nothing
            print()
        else:
            print("Unknown command given.")
        command = input("Please input a command:\n" + commandList).lower()

