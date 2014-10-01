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
            if j < len(p) and (p[j] == '?' or s[i] == p[j]): # Move to next if s[i] == p[j] or p[j] == '?'
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*': # Backup if p[j] == '*'. Keep s but move p
                j += 1
                backupS = i
                backupP = j
            else:                       # No match
                if backupP == -1:       # if no backup, return false
                    return False
                backupS += 1            # Have a backup, move backupS, restore all the backup
                i = backupS
                j = backupP

        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p) # and i == len(s)
    # Note
    # 1. Line 47 can be removed because when it's out of loop, i must == len(s)
    # 2. Line 39 doens't matter if it is backupS or backupP
