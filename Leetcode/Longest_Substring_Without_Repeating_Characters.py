"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_len = 0
        d = {}
        for i, char in enumerate(s):
            if char in d:
                start = max(start,d[char] + 1)
            d[char] = i
            max_len = max(max_len, i-start+1)
        return max_len

    # I did this totally by myself. Previous solution was wrong.

    """
    This is not incorrect, but waste too much time
    def lengthOfLongestSubstring(self, s):
        N = len(s)
        if N <= 1:
            return N
        d = {}
        max_len = 0
        cur = 0
        i = 0
        while i < N:
            if s[i] not in d:
                d[s[i]] = i
                cur += 1
                max_len = max(max_len, cur)
                i += 1
            else:
                i = d[s[i]] + 1
                d = {}
                cur = 0
        return max_len
    """
