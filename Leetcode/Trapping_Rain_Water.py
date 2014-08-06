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
        max_left = A[0]
        max_right = A[N-1]
        for i in range(N):
            max_left = max(max_left, A[i])
            left_to_right[i] = max_left
            max_right = max(max_right, A[N-1-i])
            right_to_left[N-1-i] = max_right
        water = 0
        for i in range(N):
            water += min(left_to_right[i], right_to_left[i]) - A[i] # Note here
        return water
