"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        ret = []
        dp = [True for i in range(len(s))]
        self.wordBreak_helper(0, s, dict, [], ret, dp)
        return ret

    def wordBreak_helper(self, start, s, dict, res, ret, dp):
        if start == len(s):
            ret.append(' '.join(res))
            return
        for i in range(start+1, len(s)+1):
            if s[start:i] in dict and dp[i-1]:
                res.append(s[start:i])
                beforeChange = len(ret)
                self.wordBreak_helper(i, s, dict, res, ret, dp)
                if beforeChange == len(ret):
                    dp[i-1] = False
                res.pop()

    # Use dp to reduce the duplicate
    # Another way is follow NC use divide and conquer
