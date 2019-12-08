"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        N = len(s)
        if N <= 1:
            return 0
        ret = 0
        stack = []
        last = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i + 1
                else:
                    index = stack.pop()
                    if len(stack) == 0:
                        ret = max(ret, i - last + 1)
                    else:
                        ret = max(ret, i - stack[-1])
        return ret
