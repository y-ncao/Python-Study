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
        dp = [ [0 for j in range(n)] for i in range(m) ]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    # Note:
    # 1. dp[i][j] means from (0,0) to (i, j) how many ways to finish
    # 2. init dp[i][0] = 1, dp[0][j] = 1
    # 3. dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 4. result dp[m-1][n-1]
