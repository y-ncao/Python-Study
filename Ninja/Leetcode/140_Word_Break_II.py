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

```

这两种方法本质上没有区别
* 前者是如果运行dfs之后结果没有变化，说明没有搜到，后面也不用搜了
* 后者是预处理dp然后用在recursion之中

```python

    def wordBreak(self, s, dict):
        ret = []
        dp = self.word_break_dp(s, dict)
        self.dfs_word_break(len(s)+1, s, dict, [], ret, dp)
        return ret

    def word_break_dp(self, s, dict):
        N = len(s)
        dp = [False for i in range(N+1)]
        dp[0] = True
        for i in range(N):
            for j in range(i):
                if dp[j] and s[j:i]:
                    dp[i] = True
                    break
        return dp

    def dfs_word_break(self, end, s, dict, res, ret, dp):
        if end == 0:
            ret.append(' '.join(res))
            return
        for i in range(end):
            if dp[i] and s[i:end] in dict:
                res.insert(0, s[i:end]) # Note this is insert(0)
                self.dfs_word_break(i, s, dict, res, ret, dp)
                res.pop(0)              # So this is pop(0)

        # dict = ["cat", "cats", "and", "sand", "dog"]
        # s = "catsanddog"
        # print wordBreak(s, dict)
