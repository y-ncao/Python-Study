"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        ret = []
        self.combinationSum_helper(sorted(candidates), target, [], ret) # Look into the question, need sorted
        return ret

    def combinationSum_helper(self, candidates, target, res, ret):
        if target == 0:
            ret.append(res[:])
            return
        for i, num in enumerate(candidates):
            if target >= num:
                res.append(num)
                self.combinationSum_helper(candidates[i:], target - num, res, ret)
                res.pop()

    # Improvements: only continue when target > num ,else stop
