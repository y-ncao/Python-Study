"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        start = 1
        cur = 2
        while cur < len(A):
            if A[cur] != A[start] or A[cur] != A[start-1]:
                A[start+1] = A[cur]
                start += 1
            cur+= 1
        return start+1
