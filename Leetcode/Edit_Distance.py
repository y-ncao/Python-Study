"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        A = len(word1)
        B = len(word2)
        dp = [ [ 0 for j in range(B+1)] for i in range(A+1)]
        for i in range(A+1):
            dp[i][0] = i
        for j in range(B+1):
            dp[0][j] = j
        for i in range(1, A+1):
            for j in range(1, B+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min( dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[A][B]

    # Note:
    # 1. This dp is a bit diff, the length of dp is A+1, B+1
    # 2. Others are the same, remember how to initiate the dp matrix
    # 3. When comparing the i, it compares with word[i-1] and word[j-1]
    #    This is not hard to think, since we start loop from 1
    # 4. Initial value of DP: add N chars for word1
