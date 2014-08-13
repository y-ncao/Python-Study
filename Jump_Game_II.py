"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n == 1:
            return 0
        res = 0
        start = 0
        while start < n-1:
            res += 1
            if start + A[start] >= n-1:
                return res
            max_step = start
            for i in range(start+1, start+A[start]+1):
                if i + A[i] >= max_step + A[max_step]: # Here doesn't have to be >=
                    max_step = i
            start = max_step
