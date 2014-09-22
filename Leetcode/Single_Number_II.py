"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        bits = [0 for i in range(32)]
        for i in range(32):
            for num in A:
                bits[i] += (num >> i & 1)
                bits[i] %= 3
        if bits[31] % 3 == 0:            # Positive
            for i in range(31):
                if bits[i] == 1:
                    res += 1 << i
        else:                            # Negative
            for i in range(31):
                if bits[i] == 0:
                    res += 1 << i
            res = -(res + 1)
        return res
    """
    A = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    A = [1,2,3,1,2,3,1,2,3,-4]
    print singleNumber('shit', A)
    """
    # Note:
    # Python is a little different with doing this
    # In java, int is 32 bits, so we can just play with it
    # But in python, need to check if number is positive or negative
    # So need to do line 18 to 26 check
    # Otherwise should looks like somthing

    def singleNumber(self, A):
        res = 0
        for i in range(32):
            bit = 0
            for num in A:
                bit += num >> i & 1
                bit %= 3
            res += bit << i
        return res
    A = [1,2,3,1,2,3,1,2,3,4]
    # This one works fine in python if all num > 0
