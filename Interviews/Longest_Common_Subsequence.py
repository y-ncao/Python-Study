"""
Need to distinguish from Longest Common Substring

Examples:
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.

[Solution](http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)

DP way is O(m*n)
Normal way O(m^2 *n)

1. dp[i][j] is LCS for first i chars of a and first j chars of b
2. dp[i][j] = 0
3. dp[i][j] = dp[i-1][j-1] + 1             # if a[i] == b[j]
            = max(dp[i-1][j], dp[i][j-1])  # if a[i] != b[j]
4. dp[M][N]
"""

def Longest_Common_Subsequence(a, b):
    M = len(a)
    N = len(b)
    dp = [ [0 for j in range(N+1)] for i in range(M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1] + 1

    return dp[M][N]

# Note
# 1. Very important, line 25 and 26 is range(1, X+1)

print Longest_Common_Subsequence('ABCDGH', 'AEDFHR')
print Longest_Common_Subsequence('AGGTAB', 'GXTXAYB')
print Longest_Common_Subsequence('B', 'B')
