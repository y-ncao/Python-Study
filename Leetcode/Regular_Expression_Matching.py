"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.  
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:  
bool isMatch(const char *s, const char *p)

Some examples:  
isMatch("aa","a") → false  
isMatch("aa","aa") → true  
isMatch("aaa","aa") → false  
isMatch("aa", "a*") → true  
isMatch("aa", ".*") → true  
isMatch("ab", ".*") → true  
isMatch("aab", "c*a*b") → true
"""

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        M = len(s)
        N = len(p)
        dp = [ [False for j in range(N+1)] for i in range(M+1) ]
        dp[0][0] = True
        pi = 2                          # Means pair increase, e.g. p = a*b*c*d*, s ='', should be true
        while pi < N + 1 and p[pi-1] == '*':
            dp[0][pi] = True
            pi += 2

        for i in range(1, M+1):
            for j in range(1, N+1):
                if p[j-1] == '.' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or \ # * is used as zero
                               dp[i][j-2] or \ # * is removing the previous char
                               (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')) # * is back matching

        return dp[M][N]

    # Notice
    # 1. Line 30 initializing
    # 2. Line 39 ~ 41
