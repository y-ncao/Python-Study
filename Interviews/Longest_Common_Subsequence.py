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

Keep reading for [print LCS](http://www.geeksforgeeks.org/printing-longest-common-subsequence/)
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
print '-'*10
# This is also correct, be we are storing all the results. So should do in dp way
def LCS_recur(a, b):
    if not a or not b:
        return 0
    if a[-1] == b[-1]:
        return 1 + LCS_recur(a[:-1], b[:-1])
    else:
        return max(LCS_recur(a[:-1], b), LCS_recur(a, b[:-1]))

print LCS_recur('ABCDGH', 'AEDFHR')
print LCS_recur('AGGTAB', 'GXTXAYB')
print LCS_recur('B', 'B')
print '-'*10

def LCS(a, b):
    M = len(a)
    N = len(b)
    dp = [ [0 for j in range(N+1)] for i in range(M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1] + 1

    res = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            res.insert(0, a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(res)

print LCS('ABCDGH', 'AEDFHR')
print LCS('AGGTAB', 'GXTXAYB')

"""
                0       1       2       3       4       5       6       7
                Ø       M       Z       J       A       W       X       U
0       Ø       0       0       0       0       0       0       0       0
1       X       0       0       0       0       0       0       1       1
2       M       0       1       1       1       1       1       1       1
3       J       0       1       1       2       2       2       2       2
4       Y       0       1       1       2       2       2       2       2
5       A       0       1       1       2       3       3       3       3
6       U       0       1       1       2       3       3       3       4
7       Z       0       1       2       2       3       3       3       4
"""
