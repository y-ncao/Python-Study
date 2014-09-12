"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        M = len(grid)
        N = len(grid[0])
        dp = [ [0 for j in range(N)] for i in range(M)]
        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[M-1][N-1]

    # Note:
    # 1. dp[i][j] means from (0, 0) to (i, j) the min path sum
    # 2. init: dp[i][0] = dp[i-1][0]+grid[i][j], dp[0][j] += dp[0][j-1]+grid[i][j]
    # 3. func: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    # 4. ret: dp[m-1][n-1]
"""
All Previous work. No need to worry
    def minPathSum_1(self, grid):
        M = len(grid)
        N = len(grid[0])
        dp = [[ 0 for j in range(N)] for i in range(M)]
        dp[0][0] = grid[0][0]
        for i in range(1, M):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, N):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[M-1][N-1]

    # Another time:
    # dp[m][n] dp[i][j]
    # M is the rows
    # N is the cols
    # [[for j in range(N)] for i in range(M)]
    # M = len(grid)
    # N = len(grid[0])


    Given the dynamic programming formula f[i][j]=min(f[i-1][j],f[i][j-1])+grid[i][j]:

    Assume that you are populating the table row by row, the current value (f[i][j]) will be used immediately in the calculation of f[i][j+1], so there is no need to store all the previous column values.

    Therefore, you can do it in linear space complexity.

    def minPathSum_2(self, grid):
        M = len(grid)
        N = len(grid[0])
        dp = [ 0 for j in range(N)]
        dp[0] = grid[0][0]
        for j in range(1, N):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, M):
            dp[0] += grid[i][0]
            for j in range(1, N):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[N-1]

    # This is a bit tricky. Read the above how to simplify this
    # The key is we are doing this for j ... so we can just j-1
"""
