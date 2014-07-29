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
        return self.longestConsecutive_2(num)

    # Using dict
    def longestConsecutive_1(self, num):
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

    # Not using dict
    def longestConsecutive_2(self, num):
        ret = 1
        for i in num[:]:
            if i not in num:
                continue
            length = 1
            j = i
            while j+1 in num:
                length += 1
                num.remove(j+1)
                j += 1
            j = i
            while j-1 in num:
                length += 1
                num.remove(j-1)
                j -= 1
            ret = max(ret, length)
            num.remove(i)
        return ret


# This is correct but exceeded the time limit
# This should be done in finding the num for both directions, need to remember this
"""
    def longestConsecutive_1(self, num):
        if len(num) <= 1:
            return len(num)
        dp_dict = {}
        ret = 1
        for i in num:
            j = i
            length = 1
            while j+1 in num:
                if j+1 in dp_dict:
                    length = length + dp_dict[j+1]
                    break
                length += 1
                j += 1
            ret = max(ret, length)
            dp_dict[i] = length
        return ret
"""
