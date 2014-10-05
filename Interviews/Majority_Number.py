"""
#####From mibbs for Linkedin Interview
Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:

       I/P : 3 3 4 2 4 4 2 4 4
       O/P : 4

       I/P : 3 3 4 2 4 4 2 4
       O/P : NONE
[Solution](http://www.geeksforgeeks.org/majority-element/)
"""

def majority_i(A):
    N = len(A)
    candidate = None
    count = 1
    for i in range(N):
        if candidate == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = A[i]
            count = 1

    return candidate

A = [1,2,1,2,1,2,3,2,4,2]

print majority_i(A)

def majority_ii(A):
    candidate_1 = None
    count_1 = 0
    candidate_2 = None
    count_2 = 0
    for i in range(len(A)):
        if count_1 == 0:
            candidate_1 = A[i]
        if count_2 == 0 and candidate_1 != A[i]:
            candidate_2 = A[i]
        if A[i] not in [candidate_1, candidate_2] and count_1 > 0 and count_2 > 0:
            count_1 -= 1
            count_2 -= 1
        if A[i] == candidate_1:
            count_1 += 1
        if A[i] == candidate_2:
            count_2 += 1
    if count_1 > count_2:
        return candidate_1
    else:
        return candidate_2
