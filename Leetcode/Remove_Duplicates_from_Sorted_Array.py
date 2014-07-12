"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        return self.removeDuplicates_2(A)

    def removeDuplicates_1(self, A):
        i = 0
        for j in range(len(A)):
            if i == 0 or A[j] != A[j-1]:
                A[i] = A[j]
                i += 1
        return i

    def removeDuplicates_2(self, A):
        if len(A) <= 1:
            return len(A)
        i = 0
        for j in range(1, len(A)):
            if A[i] != A[j]:
                A[i+1] = A[j]
                i += 1
        return i+1
    # Second way is my way
