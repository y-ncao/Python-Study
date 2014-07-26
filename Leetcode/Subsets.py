"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        return self.subsets_1(S)

    # Iteration method
    def subsets_1(self, S):
        ret = [[]]
        for i in sorted(S):
            res = []
            for el in ret:
                res.append(el[:])
                el.append(i)
                res.append(el[:])
            ret = res[:]
        return ret

    # Recursion method
    def subsets_2(self, S):
        ret = []
        self.subsets_helper(0, sorted(S), [], ret)
        return ret

    def subsets_helper(self, i, S, res, ret):
        if i == len(S):
            ret.append(res[:])
            return
        self.subsets_helper(i+1, S, res, ret) # No element i
        res.append(S[i])
        self.subsets_helper(i+1, S, res, ret) # With element i
        res.pop()

    # Keep in mind the sorted
