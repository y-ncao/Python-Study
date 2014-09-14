"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Note:
The answer is three rabbit by removing the first, second, third 'b'
"""

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        N = len(S)
        M = len(T)
        dp = [ [0 for j in range(N+1)] for i in range(M+1)]
        for i in range(M+1):
            dp[i][0] = 0
        for j in range(N+1):
            dp[0][j] = 1
        for i in range(1, M+1):
            for j in range(1, N+1):
                if S[j-1] == T[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[M][N]
    # Note
    # dp[i][j]表示S的前i个字符配上T的前j个字符的DS
    # [i][0] = 0, dp[0][j] = 1
    # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] # if S[i-1] == T[j-1]
    #          = dp[i][j-1]                # if S[i-1] != T[j-1]
    # dp[M][N]
