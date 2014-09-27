"""
#####Shuffle a given array
Saw it from FiveStar's interview.

Solution is from Geeksforgeesk
Fisher-Yates shuffle Algorithm works in O(n) time complexity.
"""

def shuffle_array(A):
    from random import random
    N = len(A)
    for i in range(N):
        random_num = int(random() * (N-i))
        A[N-i-1], A[random_num] = A[random_num], A[N-i-1]
    return A


A = [ i + 1 for i in range(52)]

print shuffle_array(A)

# Note
# 1. from random import random
# 2. from random import randint. randint(start, end), include start and end
