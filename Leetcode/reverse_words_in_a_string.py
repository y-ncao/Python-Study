"""
Given an input string, reverse the string word by word.

For example,
Given s = 'the sky is blue',
return 'blue is sky the'.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

"""

class Solution:
    # @param s, a string
    # @return a string

    # This is a python easy way
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
