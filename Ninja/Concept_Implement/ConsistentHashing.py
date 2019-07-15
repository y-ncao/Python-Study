'''consistent_hashing.py is a simple demonstration of consistent
hashing.'''

import bisect
import hashlib

class ConsistentHash:
    '''ConsistentHash(n,r) creates a consistent hash object for a
    cluster of size n, using r replicas.

    It has three attributes. num_machines and num_replics are
    self-explanatory.  hash_tuples is a list of tuples (j,k,hash),
    where j ranges over machine numbers (0...n-1), k ranges over
    replicas (0...r-1), and hash is the corresponding hash value,
    in the range [0,1).  The tuples are sorted by increasing hash
    value.

    The class has a single instance method, get_machine(key), which
    returns the number of the machine to which key should be
    mapped.'''

    def __init__(self,num_machines=1,num_replicas=1):
        self.num_machines = num_machines
        self.num_replicas = num_replicas
        # Key is like node1_replica2 etc
        hash_tuples = [(j,k,my_hash(str(j)+"_"+str(k))) \
                       for j in range(self.num_machines) \
                       for k in range(self.num_replicas)]
        # Sort the hash tuples based on just the hash values
        # cmp is a built-in compare function. This is used for compare the value of machines from str
        hash_tuples.sort(lambda x,y: cmp(x[2],y[2]))
        self.hash_tuples = hash_tuples

    def get_machine(self,key):
        '''Returns the number of the machine which key gets sent to.'''
        h = my_hash(key)
        # edge case where we cycle past hash value of 1 and back to 0.
        if h > self.hash_tuples[-1][2]:
            return self.hash_tuples[0][0]
        hash_values = map(lambda x: x[2],self.hash_tuples)
        # bitsect is used to find the index that we want to insert h
        # the index will be used same as finding the first clockwise node
        # https://docs.python.org/2/library/bisect.html
        index = bisect.bisect_left(hash_values,h)
        return self.hash_tuples[index][0]

def my_hash(key):
    '''my_hash(key) returns a hash in the range [0,1).'''
    return (int(hashlib.md5(key).hexdigest(),16) % 1000000)/1000000.0

def main():
    ch = ConsistentHash(7,3)
    print "Format:"
    print "(machine,replica,hash value):"
    for (j,k,h) in ch.hash_tuples: print "(%s,%s,%s)" % (j,k,h)
    while True:
        print "\nPlease enter a key:"
        key = raw_input()
        print "\nKey %s maps to hash %s, and so to machine %s" \
            % (key,my_hash(key),ch.get_machine(key))

if __name__ == "__main__": main()
