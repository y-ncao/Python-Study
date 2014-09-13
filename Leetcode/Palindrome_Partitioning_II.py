"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        N = len(s)
        dp = [ N for i in range(N)]
        dp[0] = 0
        for i in range(1, N):
            dp[i] = sys.maxint
            for j in range(i)[::-1]:
                if self.isPalindrome(s[j:i]):
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[N-1]

    def isPalindrome(self, s):
        return s == s[::-1]

    # 1. dp means from 0 ... i the mean cut of palin
    # 2. dp[0] = 0
    # 3. dp[i] = min(dp[i], dp[j]+1) for j = i-1 ... 0 if isPalin(s[j:i])
    # 4. dp[N-1]
    # This idea is correct, but next thing is to reduce the cost of isPalindrome
