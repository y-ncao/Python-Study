"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""

class Solution:
    # @return an integer
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            max_water = max(max_water, (r-l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_water

    # Two pointer problem
