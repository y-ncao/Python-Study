"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [ [0 for i in range(m)] for j in range(n)]
        for i in range(1, m):
            dp[0][i] = 1
        for j in range(1, n):
            dp[j][0] = 1
