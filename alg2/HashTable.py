###HASHTABLE CLASS


class HashTableEntry:

    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashTable:

    def print(self):
        print(*self.map)

    # Constructor
    # Space-time complexity is O(1)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # private getter to create a hash key
    # Space-time complexity is O(1)
    def _get_hash(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Insert a new package value into the hash table
    # Space-time complexity is O(N)
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Space-time complexity is O(N)
    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    # Grab a value from the hash table
    # Space-time complexity is O(N)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    # Remove a value from the hash table
    # runtime is O(N)
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False





# class HashTableItem:
#     def __init__(self,key,item):
#         self.key = key
#         self.item = item
#
# class HashTable(object):
#     def __init__(self,length=5):
#         #Default constructor with empty
#         self.array = [None] * length
#
#     def hash(self,key):
#         #Returns an index in the array for the given key
#         length = len(self.array)
#         return int(key) % length
#
#     #def addPackage(self, packageID, deliveryAddress, deliveryDeadline, deliveryCity, deliveryZip, packageWeight, deliveryStatus):
#
#     def add2(self, key, value):
#         """Add a value to our array by its key"""
#         index = self.hash(key)
#         if self.array[index] is not None:
#             # This index already contain some values.
#             # This means that this add MIGHT be an update
#             # to a key that already exist. Instead of just storing
#             # the value we have to first look if the key exist.
#             for kvp in self.array[index]:
#                 # If key is found, then update
#                 # its current value to the new value.
#                 if kvp[0] == key:
#                     kvp[1] = value
#                     break
#             else:
#                 # If no breaks was hit in the for loop, it
#                 # means that no existing key was found,
#                 # so we can simply just add it to the end.
#                 self.array[index].append([key, value])
#         else:
#             # This index is empty. We should initiate
#             # a list and append our key-value-pair to it.
#             self.array[index] = []
#             self.array[index].append([key, value])
#
#     def add(self,key,value):
#         #Adds a given value to the HashTable by the given key
#         index = self.hash(key)
#         if self.array[index] is not None:
#             """There's already some data here"""
#             for key_value_pair in self.array[index]:
#                 if key_value_pair[0]==key:
#                     key_value_pair[1]=value
#                     break
#                 else:
#                     self.array[index].append(key,value)
#             else:
#                 self.array[index]=[]
#                 self.array[index].append([key,value])
#     def get(self,key):
#         #Return a value by key
#         index = self.has(key)
#         if self.array[index] is None:
#             raise KeyError()
#         else:
#             for key_value_pair in self.array[index]:
#                 if key_value_pair[0]==key:
#                     return key_value_pair[1]
#
#             #if we didn't return one by now, its not in there
#             raise KeyError()
#
#     def bark(self):
#         print("WOOF")
#
#     def print(self):
#         print(*self.array)
