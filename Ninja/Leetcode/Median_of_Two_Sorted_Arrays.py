"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length % 2 == 0:
            return ( self.findKth(A, 0, B, 0, length / 2) + self.findKth(A, 0, B, 0, length / 2 + 1) ) / 2.0
        else:
            return self.findKth(A, 0, B, 0, length / 2 + 1)

    def findKth(self, A, A_start, B, B_start, k):
        if A_start >= len(A):
            return B[B_start + k - 1]
        if B_start >= len(B):
            return A[A_start + k - 1]

        if k == 1:
            return min(A[A_start], B[B_start])

        if A_start + k/2 -1 < len(A):
            A_key = A[A_start + k/2 -1]
        else:
            A_key = 9223372036854775807

        if B_start + k/2 -1 < len(B):
            B_key = B[B_start + k/2 -1]
        else:
            B_key = 9223372036854775807

        if A_key < B_key:
            return self.findKth(A, A_start + k / 2, B, B_start, k - k/2)
        else:
            return self.findKth(A, A_start, B, B_start + k / 2, k - k/2)

        # So manny details:
        # 1. last line is k - k/2
        # 2. Line 10, divided by 2.0 to make it float
        # 3. don't forget to -1 or +1 on some index
