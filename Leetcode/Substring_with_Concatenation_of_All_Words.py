"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

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
        LS, LL, LL0 = len(S), len(L), len(L[0])
        did, ids, dl = {}, 0, {}
        for s in L:
            id = did.get(s, -1)
            if id == -1:
                 ids = ids + 1
                 id = ids
                 did[s] = id
            dl[id] = dl.get(id, 0) + 1

        pos, ans = [0] * LS, []
        for k, v in did.items():
            f = S.find(k)
            while f != -1:
                pos[f] = v
                f = S.find(k, f + 1)

        for sp in range(LL0):
            np, pp, tot, dt = sp, sp, 0, {}
            while np < LS:
                t = pos[np]
                if t == 0:
                    tot, dt = 0, {}
                    pp, np = np + LL0, np + LL0
                elif dt.get(t, 0) < dl[t]:
                    dt[t] = dt.get(t, 0) + 1
                    tot = tot + 1
                    if tot == LL:
                        ans.append(pp)
                    np = np + LL0
                else:
                    while pos[pp] != t:
                        tot = tot - 1
                        dt[pos[pp]] -= 1
                        pp = pp + LL0
                    pp = pp + LL0
                    dt[t] -= 1
                    tot = tot - 1
        return ans

"""
        if len(S) == 0 or len(L) == 0:
            return []
        length = len(L[0])
        N = len(S)
        dp = [0 for i in range(N-length)]
        ret = 0
        for i in range(N-length):
            if S[i:length] in L:
                dp[i] = 1
                if i >= length and dp[i-length] > 0:
                    dp[i] += dp[i-length]
                ret = max(ret, dp[i])
        return ret
"""
