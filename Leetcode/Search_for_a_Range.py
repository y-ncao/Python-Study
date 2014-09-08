"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0
        end = len(A) - 1
        bound = [-1, -1]

        # Check for left bound
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            bound[0] = start
        elif A[end] == target:
            bound[0] = end
        else:
            return bound

        # Check right bound
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            bound[1] = end
        elif A[start] == target:
            bound[1] = start

        return bound
