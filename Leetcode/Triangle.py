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
