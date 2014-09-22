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
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.calculate(a, b, token))
            else:
                stack.append(int(token))
        return stack.pop()

    def calculate(self, num_1, num_2, operator):
        oper_dict = { '+' : lambda x, y: x + y,
                      '-' : lambda x, y: x - y,
                      '*' : lambda x, y: x * y,
                      '/' : lambda x, y: int( x * 1.0 / y),
                      }
        return oper_dict[operator](num_1, num_2)

    # Notice:
    # Need to be very careful about line 29, need to convert float and result is in int
