"""
Divide two integers without using multiplication, division and mod operator.
"""

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if (dividend < 0) != (divisor < 0):
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor  = abs(divisor)
        res = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= divisor << shift:
                shift += 1
            #print 'res = %d, shift = %d, adding = %d, dividend = %d' % (res, shift, 1<<(shift-1), dividend)
            res += 1 << (shift - 1)            # This is shift-1, because the top loop quit
            dividend -= divisor << (shift - 1) # when dividend < divisor << shift, so we don't want to shift more
        return res * sign

    # How to think:
    # Any number can be computed in binary way, like 8 = 2^3 * 1 + 2^2 * 0 + 2^1 * 0 + 2^0 * 0
    # In this case, we calculate this num = a * (2^n * an + ... + 2^1 * a1 + 2^0 * a0)
    # So we calculate an first, them decrease num with a * 2^an, and sum(2^i * ai)
