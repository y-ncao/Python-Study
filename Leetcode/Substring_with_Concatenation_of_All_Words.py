"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if len(S) == 0 or len(L) == 0:
            return []
        length = len(L[0])
        N = len(S)
        dp = [0 for i in range(N-length)]
        ret = 0
        for i in range(N-length):
            if S[i:length] in L:
                dp[i] = 1
                if i >= length and dp[i-length] > 0:
                    dp[i] += dp[i-length]
                ret = max(ret, dp[i])
        return ret
