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
        prev = '1'
        for i in range(1, n):
            counter = 1
            cur = [prev[0]]
            for char in prev[1:]:
                if char == cur[-1]:
                    counter += 1
                else:
                    cur.insert(-1, str(counter))
                    cur.append(char)
                    counter = 1
            cur.insert(-1, str(counter))
            prev = ''.join(cur)
        return prev
