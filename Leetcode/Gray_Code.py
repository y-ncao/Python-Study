"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""

# Tip: you can use bin(x) to check the binary form of a num

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        ret = []
        i = 0
        while i < 2**n:
            ret.append(i>>1^i)
            i+=1
        return ret

# But these two won't pass because they return binary form string not the gray code in int
"""
    def grayCodeGen(self, n, reverse=False):
        if n == 1:
            if reverse:
                yield "1"
                yield "0"
            else:
                yield "0"
                yield "1"
        else:
            if reverse:
                # all the "1"s start first
                gcprev = self.grayCodeGen(n-1, False)
                for code in gcprev:
                    yield "1" + code
                gcprev = self.grayCodeGen(n-1, True)
                for code in gcprev:
                    yield "0" + code
            else:
                # all the "0" start first
                gcprev = self.grayCodeGen(n-1, False)
                for code in gcprev:
                    yield "0" + code
                gcprev = self.grayCodeGen(n-1, True)
                for code in gcprev:
                    yield "1" + code

    # This is even better, no need to use iterator
    def grayCodeGen_2(n):
        if n == 1:
            return ['0', '1']
        else:
            ret = []
            code_list = grayCodeGen_2(n-1)
            for code in code_list:
                ret.append('0' + code)
            for code in code_list[::-1]:
                ret.append('1' + code)
        return ret
"""
