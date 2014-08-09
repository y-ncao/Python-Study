"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            if A[i] != i+1 and A[i] >= 1 and A[i] <= n and A[A[i]-1] != A[i]: # The last check is important
                self.swap(A, i, A[i]-1)
            else:
                i += 1

        for i, num in enumerate(A):
            if num != i+1:              # The check here is also very important
                return i+1
        return n + 1

    def swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    # Way to think
    # O(n) imply that we need to use hashtable
    # But it ask for constant space, so need to use the index as hashtable to store the num
