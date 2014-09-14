"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        return self.isInterleave_1(s1, s2, s3)

    def isInterleave_1(self, s1, s2, s3):
        M = len(s1)
        N = len(s2)
        K = len(s3)
        if M + N != K:
            return False
        dp = [ [ False for j in range(N+1)] for i in range(M+1) ]
        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i > 0 and dp[i-1][j] and s1[i-1] == s3[i-1+j]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[M][N]

    # Note:
    # 1. dp[i][j] means whether s1[:i] and s2[:j] is interleave with s3[:i+j]
    # 2. dp[0...M][0...N] = False
    # 3. dp[i][j] = True   # if dp[i-1][j] == True and s1[i-1] == s3[i-1+j] or
    #                           dp[i][j-1] == True and s2[j-1] == s3[i+j-1]
    #             = False  # else
    # 4. dp[M][N]

    # Will TLE
    def isInterleave_2(self, s1, s2, s3):
        return self.isInterleave_re(s1, 0, s2, 0, s3, 0)

    def isInterleave_re(self, s1, i1, s2, i2, s3, i3):
        if i1 >= len(s1) and i2 >= len(s2) and i3 >= len(s3):
            return True
        if i3 >= len(s3):
            return False
        if i1 >= len(s1):
            return s2[i2:] == s3[i3:]
        if i2 >= len(s2):
            return s1[i1:] == s3[i3:]

        return (s1[i1] == s3[i3] and self.isInterleave_re(s1, i1+1, s2, i2, s3, i3+1)) or (s2[i2] == s3[i3] and self.isInterleave_re(s1, i1, s2, i2+1, s3, i3+1))
