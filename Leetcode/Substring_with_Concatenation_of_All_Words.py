"""
You are given a string, S, and a list of words, L, that are all of the same length.
Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        M = len(L[0])
        N = len(S)
        ret = []
        i = 0
        while i < N - M + 1:
            if S[i:i+M] in L:
                tmp = L[:]
                tmp.remove(S[i:i+M])
                j = i + M
                start = None
                while len(tmp) > 0 and j + M < N and S[j:j+M] in L:
                    print 'start from here?', tmp
                    if S[j:j+M] in tmp:
                        tmp.remove(S[j:j+M])
                        j += M
                    elif start == None:

                        start = j
                        break
                if len(tmp) == 0:
                    ret.append(i)
                if start is None:
                    i = j
                else:
                    i = start
            else:
                i += 1
        return ret
