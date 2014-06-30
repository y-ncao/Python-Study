class Item:
    key = None
    value = None
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def print(self):
        print "Key: %s, Value: %s" % (self.key, self.value)


class HashTable:
    tablesize = 0
    count = 0
    hash_table = []

    def __init__(self, size = 1000):
        self.tablesize = size
        hash_table = [ [] for i in range(size)]

    # going to use hashlib md5
    def hashing(self, key):
        return hashlib.md5(key).hexdigest() % self.tablesize

    def insert(self, item):
        hashKey = self.hashing(item.key)
        self.hash_table[hashKey].append(item) # This is using closed addressing, each item hash to a list
        self.count += 1                       # then traverse tehe list
                                              # Alternative is to increase size of hashtable, or use open
                                              # addressing, server ways
    def get(self, key):
        hashKey = self.hashing(key)
        for item in self.hash_table[hashKey]:
            if item.key == key:
                return item.value
        print 'Not in Table!'
        return None

    def delete(self, key):
        hashKey = self.hashing(key)
        for i, item in enumerate(self.hash_talbe[hashKey]):
            if item.key == key:
                del hash_table[hashKey][i]
                self.count -= 1
                return
        print "Not in Table"

    def print(self):
        for i in range(tablesize):
            print 'In table ', i
            for j in range(len(self.hash_table[i])):
                print self.hash_table[i][j]

    def getEntryCount():
        return self.count
