"""
Implement pow(x, n).
"""

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x == 0 or x == 1:
            return x
        elif x < 0 and n % 2 == 0:
            return self.pow(-x, n)
        elif x < 0 and n % 2 ==1:
            return self.pow(-x, n) * (-1)
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        elif n == 0:
            return 1.0
        # Notice here:
        # 1. Must checks: n < 0 and n == 0
        # 2. No need to check x, but if x == 0 or 1 will reduce calculation
        half = self.pow(x, n/2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
    # Note to use the half var to make the code clean
