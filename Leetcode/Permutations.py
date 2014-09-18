"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return self.permute_2(num)

    def permute_1(self, num):
        ret = []
        self.permute_helper([], num, ret)
        return ret

    def permute_helper(self, res, num, ret):
        if len(num) == 0:
            ret.append(res[:])
            return

        for i, n in enumerate(num):
            res.append(n)
            self.permute_helper(res, num[:i] + num[i+1:], ret)
            res.pop()

    # Do this "inplace"
    def permute_2(self, num):
        if len(num) == 0:
            return [[]]                 # This is the tricky part
        ret = []
        for i, n in enumerate(num):
            rest_perms = self.permute_2( num[:i]+num[i+1:] )
            for perm in rest_perms:
                ret.append( [n] + perm)
        return ret
