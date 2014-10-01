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
        return self.largestRectangleArea_1(height)

    # Use stack to merge the blocks
    def largestRectangleArea_1(self, height):
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
                index = stack.pop()
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, width * height[index])
        return max_area
    # 维护一个递增序列

    # Only calculate when decrease
    def largestRectangleArea_2(self, height):
        N = len(height)
        max_area = 0
        for i in range(N):
            if i+1 < N and height[i] <= height[i+1]:
                continue
            min_height = height[i]
            j = i
            while j >= 0:
                min_height = min(min_height, height[j])
                max_area = max(max_area, min_height * (i-j+1))
                j -= 1
        return max_area
