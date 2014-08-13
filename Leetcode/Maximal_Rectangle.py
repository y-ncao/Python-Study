"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        return self.maximalRectangle_2(matrix)

    def maximalRectangle_1(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [ [ (0,0) for j in range(col)] for i in range(row) ]
        max_area = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    x = 1
                else:
                    x = dp[i][j-1][0] + 1
                if i == 0:
                    y = 1
                else:
                    y = dp[i-1][j][1] + 1

                dp[i][j] = (x, y)
                min_width = y
                for k in range(j-x+1,j+1)[::-1]:
                    min_width = min(min_width, dp[i][k][1])
                    max_area = max(max_area, min_width * (j-k+1))
        return max_area
    # From Annie's way
    # Need to note that i -> y and j -> x
    # dp[i][j] means the consecutive length to matrix[i][j]

    # Use the historical problem's O(n) way to solve once we have the dp
    def maximalRectangle_2(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return 0
        h = [0 for i in range(col+1)]
        max_area = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    h[j] = 0
                else:
                    h[j] += 1
            max_area = max(max_area, self.largestRectangleArea(h))

        return max_area

    def largestRectangleArea(self, h):
        stack = []
        max_area = 0
        for i in range(len(h)):
            count = 0
            while len(stack) > 0 and stack[-1] > h[i]:
                count += 1
                max_area = max(max_area, count * stack.pop())
            count -= 1
            while count > 0:
                stack.append(h[i])
            stack.append(h[i])
        return max_area
