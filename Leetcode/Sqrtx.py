"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        return self.sqrt_1(x)

    # NC way to do this
    def sqrt_1(self, x):
        if x <= 1:
            return x
        left = 0
        right = x
        while left + 1 < right:
            mid = (left + right) / 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                left = mid
            else:
                right = mid
        return left
    # We are looking for the smaller one

    def sqrt_2(self, x):
        left = 0                         # Here must 0, otherwise 1 won't pass
        right = x                        # Use x/2 + 1
        while left <= right:             # <=
            mid = (left + right) / 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                left = mid + 1
            else:
                right = mid - 1
        return (left + right) / 2           # This is so important
    # On the end, we can return right, or recalculate the mid, very important
