"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            d.setdefault(key,[]).append(s)
        ret = []
        for key in d:
            if len(d[key]) > 1:
                ret.extend(d[key])
        return ret
    # Note:
    # 1. Need to use extend here, return those len(d[key]) > 1
    # 2. Need to remember the definition of Anagrams
