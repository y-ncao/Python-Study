"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = 'leetcode',
dict = ['leet', 'code'].

Return true because 'leetcode' can be segmented as 'leet code'.
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
