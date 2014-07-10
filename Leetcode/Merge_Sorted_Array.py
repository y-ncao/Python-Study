"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
"""

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        x = m + n - 1
        while i>=0 and j>=0:
            if A[i] > B[j]:
                A[x] = A[i]
                i -= 1
            else:
                A[x] = B[j]
                j -= 1
            x -= 1
        while j>=0:
            A[x] = B[j]
            x -= 1
            j -= 1
    # Focus on detail!!!
