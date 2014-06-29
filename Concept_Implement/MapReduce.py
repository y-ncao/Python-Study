#word_count.py

import string
import map_reduce

def mapper(input_key,input_value):
    return [(word,1) for word in
            remove_punctuation(input_value.lower()).split()]

def remove_punctuation(s):
    return s.translate(string.maketrans("",""), string.punctuation)

def reducer(intermediate_key,intermediate_value_list):
    return (intermediate_key,sum(intermediate_value_list))

filenames = ["text\\a.txt","text\\b.txt","text\\c.txt"]
i = {}
for filename in filenames:
    f = open(filename)
    i[filename] = f.read()
    f.close()

print map_reduce.map_reduce(i,mapper,reducer)
"""
The map_reduce module imported by this program implements MapReduce in pretty much the simplest possible way, using some useful functions from the itertools library:
"""

# map_reduce.py
"""Defines a single function, map_reduce, which takes an input
dictionary i and applies the user-defined function mapper to each
(input_key,input_value) pair, producing a list of intermediate
keys and intermediate values.  Repeated intermediate keys then
have their values grouped into a list, and the user-defined
function reducer is applied to the intermediate key and list of
intermediate values.  The results are returned as a list."""

import itertools

def map_reduce(i,mapper,reducer):
    intermediate = []
    for (key,value) in i.items():
        intermediate.extend(mapper(key,value))
    groups = {}
    # very important step.
    # 1. lambda simply yeilds the first argument in the intermdediate, which is the key.
    #    That is used for setup group by what
    # 2. sorted is used to get the result grouped. See the later comment
    # 3. line 50 list comprehension is used toe get the value, which can also use x[1] I think
    for key, group in itertools.groupby(sorted(intermediate),lambda x: x[0]):
        groups[key] = list([y for x, y in group])
    # And finally apply reducer function to each item
    return [reducer(intermediate_key,groups[intermediate_key]) for intermediate_key in groups]

"""
from itertools import groupby

def groupby_even_odd(items):
    f = lambda x: 'even' if x % 2 == 0 else 'odd'
    gb = groupby(items, f)
    for k, items in gb:
        print '%s: %s' % (k, ','.join(map(str, items)))

>>> groupby_even_odd([1, 3, 4, 5, 6, 8, 9, 11])
odd: 1,3
even: 4
odd: 5
even: 6,8
odd: 9,11

Which is not what we want. To improve, simply do the following:

def groupby_even_odd(items):
    f = lambda x: 'even' if x % 2 == 0 else 'odd'
    gb = groupby(sorted(items, key=f), f)
    for k, items in gb:
        print '%s: %s' % (k, ','.join(map(str, items)))
>>> groupby_even_odd([1, 3, 4, 5, 6, 8, 9, 11])
even: 4,6,8
odd: 1,3,5,9,11
"""
