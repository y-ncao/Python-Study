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
        if N < M:
            return ''
        need = dict.fromkeys(T, 0)
        find = dict.fromkeys(T, 0)
        for i, char in enumerate(T):
            need[char] += 1
        start = 0
        end = 0
        res_start = -1
        res_end = N
        count = 0
        while end < N:
            if S[end] not in need:
                end += 1
                continue
            if find[S[end]] < need[S[end]]:
                count += 1
            find[S[end]] += 1
            if count != M:
                end += 1
                continue
            while start < end:
                if S[start] not in need:
                    start += 1
                    continue
                if find[S[start]] == need[S[start]]:
                    break
                find[S[start]] -= 1
                start += 1
            if end - start < res_end - res_start:
                res_end = end
                res_start = start
            end += 1
        if res_start == -1:
            return ''
        else:
            return S[res_start: res_end+1]

    # Whole bunch of things can be improved from here
