"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        dp = [ [0 for j in range(N)] for i in range(M) ]
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[M-1][N-1]

    # Note:
    # Same to unique path I but more steps to initialize
