"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        A = len(a)
        B = len(b)
        res = []
        carry = 0
        i = 1
        while i <= max(A,B):            # using sum at first, then add bit if exist, this is good
            sum = carry
            if i <= A:
                sum += int(a[-i])
            if i <= B:
                sum += int(b[-i])
            bit = sum % 2
            carry = sum / 2
            i += 1
            res.insert(0, str(bit))
        if carry > 0:
            res.insert(0, '1')
        return ''.join(res)
    # Nothing would be better than this
