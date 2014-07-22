"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        ret =[]
        self.combine_helper(1, n, k, [], ret)
        return ret

    def combine_helper(self, cur, n, k, res, ret):
        if len(res) == k:
            ret.append(res[:])
            return
        for i in range(cur, n+1):
            res.append(i)
            self.combine_helper(i+1, n, k, res, ret)
            res.pop()
