"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        N = len(A)
        if N == 0:
            return 0
        left_to_right = [0 for i in range(N)]
        right_to_left = [0 for i in range(N)]
        left_to_right[0] = A[0]
        right_to_left[-1] = A[-1]

        for i in range(1, N):
            left_to_right[i] = max(left_to_right[i-1], A[i])
            right_to_left[-i-1] = max(right_to_left[-i], A[-i-1])

        water = 0
        for i in range(N):
            water += min(left_to_right[i], right_to_left[i]) - A[i] # Note here
        return water
