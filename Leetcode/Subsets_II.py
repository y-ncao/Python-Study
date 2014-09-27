"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        return self.subsetsWithDup_2(S)

    # Iteration way
    def subsetsWithDup_1(self, S):
        ret = [[]]
        for i in sorted(S):
            res = []
            for el in ret:
                if len(el) == 0 or el[-1] != i: # Check len(el) == 0
                    res.append(el[:])           # if == 0 no el[-1]
                el.append(i)                    # if el[-1] != 1, then append(el[:])
                res.append(el[:])
            ret = res
        return ret

    # Recursion way
    def subsetsWithDup_2(self, S):
        ret = []
        self.subsetsWithDup_rec(sorted(S), [], ret)
        return ret

    def subsetsWithDup_rec(self, S, res, ret):
        ret.append(res[:])

        for i, el in enumerate(S):
            if i > 0 and S[i] == S[i-1]:
                continue
            res.append(el)
            subsetsWithDup_rec(S[i+1:], res, ret)
            res.pop()
