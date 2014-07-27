"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return self.lengthOfLastWord_3(s)

    def lengthOfLastWord_1(self, s):
        if len(s.strip()) == 0:                   # Need to check if len(s) is 0
            return 0
        return len(s.strip().split()[-1])         # Python way

    def lengthOfLastWord_2(self, s):              # My way
        n = len(s) - 1
        while n >= 0 and s[n] == ' ':
            n -= 1
        i = 0
        while n >= 0 and s[n] != ' ':
            n -= 1
            i += 1
        return i

    def lengthOfLastWord_3(self, s):              # Annie way
        n = len(s) - 1
        res = 0
        while n >= 0:
            if s[n] != ' ':
                res += 1
            elif res > 0:
                break
            n -= 1
        return res
