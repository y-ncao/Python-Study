"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
"""

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        i = 0
        j = 0
        backupS = -1
        backupP = -1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                while j < len(p) and p[j] == '*':
                    j += 1
                if j == len(p):
                    return True
                backupS = i
                backupP = j
            else:
                if backupS == -1:
                    return False
                i = backupS + 1
                backupS += 1
                j = backupP
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p) and i == len(s)


    def isMatch_helper(self, s, i1, p, i2):
        S = len(s)
        P = len(p)
        if i1 >= S and i2 >= P:
            return True
        elif i2 >= P:
            return False
        elif i1 >= S and p[i2] == '*':
            return self.isMatch_helper(s, i1, p, i2+1)
        elif p[i2] == '?':
            return self.isMatch_helper(s, i1+1, p, i2+1)
        elif p[i2] == '*':
            return self.isMatch_helper(s, i1+1)
