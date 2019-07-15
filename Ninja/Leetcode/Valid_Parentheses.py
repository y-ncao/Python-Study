"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        bracket_dict = { '[' : ']',
                         '{' : '}',
                         '(' : ')',
                         }
        stack = []
        for bracket in s:
            if bracket in bracket_dict.keys():
                stack.append(bracket)
            elif len(stack) == 0 or bracket !=bracket_dict[stack.pop()]:
                return False
        return len(stack) == 0

    # Note return len(stack) == 0 not True!
