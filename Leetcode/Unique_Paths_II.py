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

        dp = [[0 for j in range(N)] for i in range(M)]
        dp[0][0] = 1
        for i in range(1, M):
            if dp[i-1][0] == 0 or obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        for j in range(1, N):
            if dp[0][j-1] == 0 or obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[M-1][N-1]
