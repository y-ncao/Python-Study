"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        operators = '+-*/'
        for i, token in enumerate(tokens):
            if token in operators:
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(self.calculate(num_1, num_2, token))
            else:
                stack.append(int(token))
        return stack[0]

    def calculate(self, num_1, num_2, token):
        if token == '+':\
            return num_1 + num_2
        if token == '-':
            return num_1 - num_2
        if token == '*':
            return num_1 * num_2
        if token == '/':
            return int(num_1 * 1.0 / num_2) # This is the trick part, need to notice
