"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
import sys
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        is_palin = self.get_is_palindrome(s)
        N = len(s)
        dp = [ N-1 for i in range(N+1)]
        dp[0] = 0
        for i in range(1, N+1):
            dp[i] = 9223372036854775807
            for j in range(i)[::-1]:
                if is_palin[j][i-1]:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[N] - 1

    def get_is_palindrome(self, s):
        N = len(s)
        is_palin = [ [ False for j in range(N)] for i in range(N) ]
        for i in range(N):
            is_palin[i][i] = True

        for i in range(N-1):
            is_palin[i][i+1] = s[i] == s[i+1]

        length = 2
        while length < N:
            start = 0
            while start + length < N:
                is_palin[start][start+length] = is_palin[start+1][start+length-1] and s[start] == s[start+length]
                start += 1
            length += 1
        return is_palin

    """
    This func is no longer used
    def is_palin(s):
        return s == s[::-1]
    """
    # 1. dp means from 0 ... i the min cut times of palin
    # 2. dp[0] = 0
    # 3. dp[i] = min(dp[i], dp[j]+1) for j = i-1 ... 0 if isPalin(s[j:i])
    # 4. dp[N] - 1

    # get_is_palindrome is used to reduce the cost for line 21
    # it's returning dp[N] - 1, very tricky
    # Beacause in definition, we define as min cut times of palin
    # But actually, we just want the min cut
    # abbacdc
    # dp[3] = 0 but actually dp[3] = 1. So dp[N] = 1 + 1 = 2 but should be 1
    # We need to reduce a delete here
