"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)                # append 0 to the end, used to find the last
        N = len(height)
        stack = []
        max_area = 0
        i = 0
        while i < N:
            if len(stack) == 0 or height[i] >= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()     # h = height[index]
                if len(stack) == 0:
                    width = i           # left bound = 0, right bound i-1, w = (i-1) - (0) + 1 = i
                else:
                    width = i - stack[-1] - 1 # left bound = stack[-1] + 1, right bound = i-1, w = (i-1) - (stack[-1] + 1) + 1 = i - stack[-1] - 1
                max_area = max(max_area, width * height[index])
        return max_area
