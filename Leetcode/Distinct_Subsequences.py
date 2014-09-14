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
        M = len(T)
        N = len(S)
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
    # !!!!分清M,i和N,j分别对应T和S哪个
    # Note:
    # dp[i][j]表示S的前i个字符配上T的前j个字符的DS
    # [i][0] = 0, dp[0][j] = 1
    # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] # if T[i-1] == S[j-1]
    #          = dp[i][j-1]                # if T[i-1] != S[j-1]
    # dp[M][N]
    # Need to draw this pic when solving this problem
    # 大概意思就是， 因为算的是S的子串和T匹配的方法， 所以一旦S[:j-1]和T[:i]有x种匹配方法时
    # S[:j]必定也至少和T[:i]有x种匹配方法，但尤其当S[j-1]==T[i-1]的时候，需要再加上S[:j-1]和T[:i-1]的匹配方法数
    #     r a b b b i t
    #   1 1 1 1 1 1 1 1
    # r 0 1 1 1 1 1 1 1
    # a 0 0 1 1 1 1 1 1
    # b 0 0 0 1 2 3 3 3
    # b 0 0 0 0 1 3 3 3
    # i 0 0 0 0 0 0 3 3
    # t 0 0 0 0 0 0 0 3
    # No matter T[i-1] ?= S[j-1],  dp[i][j] = dp[i][j-1]
    # But    if T[i-1] == S[j-1], we can add another one which is dp[i-1][j-1]
