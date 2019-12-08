"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num_dict = {}
        for i in num:
            if i not in num_dict:
                num_dict[i] = True
        ret = 1
        for i in num:
            if i not in num_dict:
                continue
            length = 1
            j = i
            while j + 1 in num_dict:
                length += 1
                num_dict.pop(j+1, None)
                j += 1
            j = i
            while j - 1 in num_dict:
                length += 1
                num_dict.pop(j-1, None)
                j -= 1
            ret = max(ret, length)
            num_dict.pop(i, None)
        return ret
    # Other methods are not O(n) solution
