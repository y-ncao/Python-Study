"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution:
    # @return a string
    def minWindow(self, S, T):
        N = len(S)
        M = len(T)
        wanted = {}
        found = {}
        for char in T:
            wanted[char] = wanted.get(char, 0) + 1
            found[char] = 0
        l = 0
        res = ''
        counter = 0
        for r in range(N):
            if S[r] not in wanted:
                continue

            found[S[r]] += 1
            if found[S[r]] <= wanted[S[r]]:
                counter += 1

            if counter == M:
                while l < r:
                    if S[l] not in wanted:
                        l += 1
                        continue
                    if found[S[l]] > wanted[S[l]]:
                        found[S[l]] -= 1
                        l += 1
                        continue
                    break
                if not res or len(res) > r - l + 1:
                    res = S[l:r+1]
        return res

    # Note
    # 1. Prepare for wo dict
    # 2. Skip chars that we don't care, increase right bound
    # 3. If current window contains all the chars we want(counter == M), stop and resize left bound
    # 4. Skip chars that we don't care. If extra chars in found > wanted, skip them
    # 5. break here
    # 6. Calculate the current size
