"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        ret = []
        self.partition_helper(s, res, ret)
        return ret

    def partition_helper(self, s, res, ret):
        N = len(s)
        if N == 0 :
            ret.append(res[:])
            return
        for i in range(1, N+1):         # This N+1 is important
            if self.is_palindrome(s[:i]):
                res.append(s[:i])
                self.partition_helper(s[i:], res, ret)
                res.pop()

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    # This function can use return s == s[::-1] to replace.
