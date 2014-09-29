"""
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        H = len(haystack)
        N = len(needle)
        if N == 0:
            return haystack
        i = 0
        while i < H - N + 1:
            if haystack[i] == needle[0]:
                start = None            # Use None here
                j = 1
                while j < N and haystack[i+j] == needle[j]:
                    if start == None and haystack[i+j] == needle[0]: # Find first dup occurance
                        start = i + j
                    j += 1
                if j == N:
                    return haystack[i:]
                if start is not None:
                    i = start
                else:
                    i = i + j
            else:
                i += 1
        return None
    # Note:
    # line 32, don't forget the i += 1