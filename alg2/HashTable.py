# HASHTABLE CLASS
# kept somewhat generic
###TODO:  DONE!!!

class HashTable:
    # Just a convenience method to print out the whole table
    def print(self):
        print(*self.hashtable)
    # Constructor
    # space-time complexity O(1)
    def __init__(self, size=40):
        # initialize the hash table with empty bucket list entries.
        self.hashtable = []
        for kvp in range(size):
            self.hashtable.append([])
    # Getter to generate a key
    # space-time complexity O(1)
    def _get_hashkey(self, key):
        return int(key) % len(self.hashtable)
    # Inserts a new PackageEntry into the HashTable
    # space-time complexity O(N)
    def insert(self, key, value):
        kv = [key, value]
        hashkey = self._get_hashkey(key)
        # Brand new insertion
        if self.hashtable[hashkey] is None:
            self.hashtable[hashkey] = kv
            return True
        else:
            # Overwrite any previous value
            for kvp in self.hashtable[hashkey]:
                if kvp[0] == key:
                    kvp[1] = kv
                    return True
            self.hashtable[hashkey].append(kv)
            return True
    # Remove a value from the hash table
    # runtime is O(N)
    def delete(self, key):
        hashkey = self._get_hashkey(key)
        # Nothing to delete
        if self.hashtable[hashkey] is None:
            return False
        # Search the whole table for the key
        for kvp in range(0, len(self.hashtable[hashkey])):
            if self.hashtable[hashkey][kvp][0] == key:
                self.hashtable[hashkey].pop(kvp)
                return True
        # Was none
        return False
    # Returns a value associated with a key
    # space-time complexity O(N)
    def get(self, key):
        hashkey = self._get_hashkey(key)
        if self.hashtable[hashkey] is not None:
            for kvp in self.hashtable[hashkey]:
                if kvp[0] == key:
                    return kvp[1]
        # Couldn't find a value
        return None
    # Update a KVP
    # space-time complexity O(N)
    def update(self, key, value):
        hashkey = self._get_hashkey(key)
        if self.hashtable[hashkey] is not None:
            for kvp in self.hashtable[hashkey]:
                if kvp[0] == key:
                    kvp[1] = value
                    return True
        else:
            print('ERROR ON UPDATE KEY: ' + key)

