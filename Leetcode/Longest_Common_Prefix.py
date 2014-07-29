"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        N = len(strs)
        compare = strs[0]
        for i in range(len(compare)):
            for str in strs[1:]:
                if len(str) == i or str[i] != compare[i]:
                    return compare[:i]
        return compare
