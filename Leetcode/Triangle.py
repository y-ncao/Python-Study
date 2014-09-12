"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        M = len(triangle)
        N = len(triangle[-1])
        dp = [ [ 0 for j in range(N)] for i in range(M)]
        for i in range(M)[::-1]:
            for j in range(len(triangle[i])):
                if i == M-1:
                    dp[i][j] = triangle[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
    # Notes:
    # This is not the best solution. But easier to understand
    # 1. status: ```dp[x][y]```表示从bottom走到top每个坐标的最短路径
    # 2. function: dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    # 3. initialize: dp[-1][j] = triangle[-1][j]
    # 4. answer: dp[0][0]

    #This is older way, but still pretty good
    def minimumTotal_2(self, triangle):
        n = len(triangle) - 1
        dp = triangle[n]
        n -= 1
        while n >= 0:
            for i in range(n+1):
                dp[i] = triangle[n][i] + min(dp[i], dp[i+1])
            n -= 1
        return dp[0]

    # This look too simple
    # Understand of this:
    # 1. From bottom to top
    # 2. transfer func: dp[i] = triangle[n][i] + min(dp[i], dp[i+1])
    #    top level dp[i] = current triangle value + min(bottom level reachable dps)
