"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        return self.search_1(A, target)

    def search_1(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if target == A[mid]:
                return mid
            if A[start] <= A[mid]:                          # First half sorted
                if target >= A[start] and target < A[mid]:  # In first half
                    end = mid - 1
                else:                                       # In second half
                    start = mid + 1
            else:                                           # Second half sorted
                if target > A[mid] and target <= A[end]:    # In second half
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
    # Very important trap here
    # Line 25
    # A[mid] > A[end] or A[start] <= A[mid] will pass
    # But not A[start] < A[mid]
    # Bescause there's a chance that mid = start

    def search_rec(self, A, target):
        return self.search_helper(A, target, 0, len(A) - 1)

    def search_helper(self, A, target, start, end):
        if start > end:
            return -1
        mid = (start  + end) / 2
        if A[mid] == target:
            return mid
        elif A[mid] > A[end]:         # First half sorted
            if A[start] <= target and target < A[mid]:
                return self.search_helper(A, target, start, mid - 1)
            else:
                return self.search_helper(A, target, mid + 1, end)
        else:                           # Second half sorted
            if A[mid] < target and target <= A[end]:
                return self.search_helper(A, target, mid + 1, end)
            else:
                return self.search_helper(A, target, start, mid - 1)
