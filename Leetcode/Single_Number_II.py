"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bits = [0 for i in range(32)]
        for num in A:
            i = 0
            while num > 0:
                bits[i] += num & 1
                i += 1
                num >>= 1
        for bit in bits:
            bit %= 3
            ret += bit
            ret >>= 1
        ret <<= 1
        return ret
