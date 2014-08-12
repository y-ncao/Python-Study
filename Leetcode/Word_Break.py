"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        return self.wordBreak_1(s, dict)

    def wordBreak_1(self, s, dict):
        N = len(s)
        dp = [False for i in range(N+1)]
        dp[0] = True
        for i in range(1, N+1):
            for k in range(0,i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
                    break
        return dp[N]
    # DP way:
    # Transfer function
    # dp[i] == True only:
    # 1. s[:i] in dict
    # 2. dp[k] == True and s[k:i] in dict
    # And actually, s[:i] in dict is a special case of dp[0] and s[0:i] in dict

    # Naive solution, won't pass
    def wordBreak_2(self, s, dict):
        N = len(s)
        if N == 0:
            return True

        for i in range(1, N+1):
            if s[:i] in dict and self.wordBreak(s[i:], dict):
                return True
        return False
