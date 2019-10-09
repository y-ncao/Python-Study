#!/usr/bin/env python

a = [1, 3, 4, 5, 7, 8, 10, 12]

def binary_search_1(a, target):
    N = len(a)
    l = 0
    r = N - 1
    while l + 1 < r:
        mid = (l + r) / 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            l = mid
        else:
            r = mid
    print l, r

def binary_search_2(a, target):
    N = len(a)
    l = 0
    r = N - 1
    while l < r:
        mid = (l + r) / 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    print l, r

binary_search_1(a, 6)
'''
Will find that binary search 1 is better
BS 2 when stop, in most case l = r, and target might smaller than l = r or bigger.
BS 1 when stop, we must have l < target < r, and l = r + 1, so we must have a interval.
With this interval, we can do what we want.
'''
