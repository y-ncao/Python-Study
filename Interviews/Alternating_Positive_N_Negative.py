"""
or Rearrange Array Alternating Positive Negative Items
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance.

Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Example:

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

Found online, also NC has marked this to high frequency

[Solution](http://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/)
"""

def rearrange_array(A):
    start  = 0
    while start < len(A) - 1:
        if start % 2 == 0 and A[start] > 0:
            i = start + 1
            while i < len(A) and A[i] >= 0:
                i += 1
            if i == len(A):
                break
            value = A[i]
            del A[i]
            A.insert(start, value)
        elif start % 2 == 1 and A[start] < 0:
            i = start + 1
            while i < len(A) and A[i] <= 0:
                i += 1
            if i == len(A):
                break
            value = A[i]
            del A[i]
            A.insert(start, value)
        start += 1
    return A

A = [1, 2, 3, -4, -1, 4]
print rearrange_array(A)
B = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print rearrange_array(B)
print '-' * 10

def rearrange_array_rotate(A):
    N = len(A)
    for i in range(N-1):
        if (i % 2 == 0 and A[i] > 0) or (i % 2 == 1 and A[i] < 0):
            next = find_next(i, A)
            if next == len(A):
                break
            rotate(i, next, A)
    return A

def find_next(i, A):
    if i % 2 == 0:
        find_negative = -1
    else:
        find_negative = 1
    start = i + 1
    while start < len(A) and A[start] * find_negative <= 0:
        start += 1
    return start

def rotate(i, next, A):
    tmp = A[next]
    while next > i:
        A[next] = A[next-1]
        next -= 1
    A[i] = tmp

A = [1, 2, 3, -4, -1, 4]
print rearrange_array_rotate(A)
B = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print rearrange_array_rotate(B)
