"""
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        return self.strStr_2(haystack, needle)

    def strStr_1(self, haystack, needle):
        M = len(haystack)
        N = len(needle)
        if N == 0:
            return haystack             # Note here
        for i in range(M-N+1):
            if haystack[i] != needle[0]:
                continue
            else:
                ret = True
                for j in range(N):
                    if haystack[i+j] != needle[j]:
                        ret = False
                        break
                if ret:
                    return haystack[i:]
        return None
    # O(m*n) way

    # KMP way, which is my final way
    def strStr_2(self, haystack, needle):
        H = len(haystack)
        N = len(needle)
        if N == 0:
            return haystack
        i = 0
        while i < H - N + 1:
            if haystack[i] == needle[0]:
                start = None            # Use None here
                j = 1
                while j < N:
                    if haystack[i+j] != needle[j]:
                        break
                    elif start is None and haystack[i+j] == needle[0]: # Find first dup occurance
                        start = i + j
                    j += 1
                if j == N:
                    return haystack[i:]
                if start is not None:
                    i = start - 1       # Detail, need to check start - 1
                else:
                    i = i + j - 1
            i += 1
        return None
    # Note:
    # 1. Note line 53 and 54, minus one there, but in interview, probably do i += 1 in else will be better
    # 2. Both ways will pass