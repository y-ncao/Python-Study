"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return True
            elif A[start] < A[mid]:     # First half sorted
                if A[start] <= target and target < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif A[start]> A[mid]:      # Second half sorted
                if A[mid] < target and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1
        return False
