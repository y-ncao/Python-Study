

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
        self.hash_table[hashKey].append(item)
        self.count += 1

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
                return
        print "Not in Table"
