###HASHTABLE CLASS
class HashTable(object):
    def __init__(self,length=5):
        #Default constructor with empty
        self.array = [None] * length

    def hash(self,key):
        #Returns an index in the array for the given key
        length = len(self.array)
        return hash(key) % length

    #def addPackage(self, packageID, deliveryAddress, deliveryDeadline, deliveryCity, deliveryZip, packageWeight, deliveryStatus):


    def add2(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)
        if self.array[index] is not None:
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for kvp in self.array[index]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # If no breaks was hit in the for loop, it
                # means that no existing key was found,
                # so we can simply just add it to the end.
                self.array[index].append([key, value])
        else:
            # This index is empty. We should initiate
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])

    def add(self,key,value):
        #Adds a given value to the HashTable by the given key
        index = self.hash(key)
        if self.array[index] is not None:
            """There's already some data here"""
            for key_value_pair in self.array[index]:
                if key_value_pair[0]==key:
                    key_value_pair[1]=value
                    break
                else:
                    self.array[index].append(key,value)
            else:
                self.array[index]=[]
                self.array[index].append([key,value])
    def get(self,key):
        #Return a value by key
        index = self.has(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for key_value_pair in self.array[index]:
                if key_value_pair[0]==key:
                    return key_value_pair[1]

            #if we didn't return one by now, its not in there
            raise KeyError()

    def bark(self):
        print("WOOF")

    def print(self):
        print(*self.array)
