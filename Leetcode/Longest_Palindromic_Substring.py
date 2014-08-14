"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        N = len(s)
        dp = [ [ False for j in range(N)] for i in range(N)]
        max_length = 0
        ret = s[0]
        # dp[i][j] means s[i:j] is palindrome
        for j in range(N):
            for i in range(j):
                dp[i][j] == (s[i] == s[j] and ( j - i < 2 or dp[i+1][j-1]))
                if dp[i][j] and max_length < j-i+1:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        ret = s[i:j]
            dp[j][j] = True
        return ret

"""
    def longestPalindrome(self, s):
        longest, mid = "", (len(s) - 1) / 2
        i, j = mid, mid
        while i >= 0 and j < len(s):
            args = [(s, i, i), (s, i, i + 1), (s, j, j), (s, j, j + 1)]
            for arg in args:
                tmp = self.longestPalindromeByAxis(*arg)
                if len(tmp) > len(longest):
                    longest = tmp
            if len(longest) >= i * 2:
                return longest
            i, j = i - 1, j + 1
        return longest

    def longestPalindromeByAxis(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return s[left + 1 : right]

    def longestPalindrome(self, s):
        arr = ['$', '#']
        for i in range(len(s)):
            arr.append(s[i])
            arr.append('#')
        p = [0] * len(arr)
        mx, pos, ansp = 0, 0, 0
        for i in range(1, len(arr)):
            p[i] = min(mx - i, p[2 * pos - i]) if mx > i else 1
            while p[i] + i < len(arr) and arr[i + p[i]] == arr[i - p[i]]:
                p[i] += 1
            if p[i] + i > mx:
                mx, pos = p[i] + i, i
            if p[i] > p[ansp]:
                ansp = i
        st = (ansp - p[ansp] + 1) // 2
        return s[st:st + p[ansp] - 1]
"""
