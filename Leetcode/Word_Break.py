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
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[N]
    # Note:
    # 1. dp[i] means from char 0 to char i-1 can be break
    # 2. dp[0] = 0
    # 3. dp[i] = for j (i-1, ... 0) if dp[j] and s[j:i] in dict
    # 4. dp[N] !!! Very important here it's N not N-1


    # Naive solution, won't pass
    def wordBreak_2(self, s, dict):
        N = len(s)
        if N == 0:
            return True

        for i in range(1, N+1):
            if s[:i] in dict and self.wordBreak(s[i:], dict):
                return True
        return False
