"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ret = []
        self.generateParenthesis_helper(n, n, '', ret)
        return ret

    def generateParenthesis_helper(self, left, right, res, ret):
        if left == 0 and right ==0:
            ret.append(res[:])
            return
        if left > 0:
            self.generateParenthesis_helper(left-1, right, res+'(', ret)
        if right > left:
            self.generateParenthesis_helper(left, right-1, res+')', ret)
