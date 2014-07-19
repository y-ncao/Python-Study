"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        return self.permuteUnique_2(num)

    def permuteUnique_1(self, num):
        ret = []
        self.permuteUnique_helper(num, [], ret)
        return ret

    def permuteUnique_helper(self, num, res, ret):
        if len(num) == 0:
            ret.append(res[:])
            return
        unique_perm = {}
        for i, n in enumerate(num):
            if n not in unique_perm:
                unique_perm[n] = True
                res.append(n)
                self.permuteUnique_helper(num[:i]+num[i+1:], res, ret)
                res.pop()
        # This is miracle to do this correctly in one time

    def permuteUnique_2(self, num):
        if len(num) == 0:
            return [[]]
        unique_perm = {}
        ret = []
        for i, n in enumerate(num):
            if n not in unique_perm:
                unique_perm[n] = True
                rest_perms = self.permuteUnique_2(num[:i]+num[i+1:])
                for perm in rest_perms:
                    ret.append([n,]+perm)
        return ret
