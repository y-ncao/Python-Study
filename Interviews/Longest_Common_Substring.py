"""
##### 9/4/2014 Interview with Tubular
1. Subset(second le)
2. LCS

Given two strings 'X' and 'Y', find the length of the longest common substring.
For example, if the given strings are "GeeksforGeeks" and "GeeksQuiz",
the output should be 5 as longest common substring is "Geeks"

[Solution](http://www.geeksforgeeks.org/longest-common-substring/)

DP is O(n^2)
Normal way would be O(n * m^2)

1. dp is LCS of first i-1 chars in a ends with char i-1 and first j-1 chars in b ends with char j-1
2. init dp[i][j] = 0
3. dp[i][j] = dp[i-1][j-1] + 1 # if a[i] == b[j]
              0                # if a[i] != b[j]
4. max(dp[0...M][0...N])
"""

def longest_common_substring(a,b):
    M = len(a)
    N = len(b)
    dp = [ [ 0 for j in range(N+1)] for i in range(M+1) ]
    res = 0

    for i in range(1, M+1):
        for j in range(1, N+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    return res

# "abcdefg"
print longest_common_substring("abc", "abz")
print longest_common_substring("abcdefgabyzzkabcde", "zzzzzzgabyzzabcabcdefg")
print longest_common_substring("GeeksforGeeks", "GeeksQuiz")
