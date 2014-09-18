"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        ret = []
        self.combinationSum_helper(sorted(candidates), target, [], ret) # Look into the question, need sorted
        return ret

    def combinationSum_helper(self, candidates, target, res, ret):
        if target == 0:
            ret.append(res[:])
            return
        for i, num in enumerate(candidates):
            if target < num or (i > 0 and num == candidates[i-1]):
                continue
            res.append(num)
            self.combinationSum_helper(candidates[i+1:], target - num, res, ret)
            res.pop()

    # Note some diffs with I:
    # 1. line 32 check dup
    # 2. line 35 [i+1:]
