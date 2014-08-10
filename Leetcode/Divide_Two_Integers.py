"""
Divide two integers without using multiplication, division and mod operator.
"""

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if ( dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend = abs(dividend)
        divisor  = abs(divisor)
        ret = 0
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                ret += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return ret * sign
