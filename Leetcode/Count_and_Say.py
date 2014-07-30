"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

class Solution:
    # @return a string
    def countAndSay(self, n):
        num = '1'
        while n > 1:
            prev = num[0]
            count = 1
            new_num = ''
            for bit in num[1:]:
                if bit == prev:
                    count += 1
                else:
                    new_num += str(count) + str(prev)
                    count = 1
                prev = bit
            new_num += str(count) + str(prev)
            num = new_num
            n -= 1
        return num
