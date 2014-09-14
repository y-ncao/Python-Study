"""
##### 9/4/2014 Interview with Tubular
1. Subset(秒了)
2. LCS

Solution see http://www.geeksforgeeks.org/longest-common-substring/

DP is O(n^2)
Normal way would be O(n*m^2)
"""

def longest_common_substring(a,b):
    m = len(a)
    n = len(b)
    dp = [ [ 0 for i in range(n+1)] for j in range(m+1) ]
    res = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    return res

# "abcdefg"
print(longest_common_substring("abc", "abz"))
print(longest_common_substring("abcdefgabyzzkabcde", "zzzzzzgabyzzabcabcdefg"))
