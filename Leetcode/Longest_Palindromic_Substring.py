"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        N = len(s)
        dp = [ [ False for j in range(N)] for i in range(N) ]
        for i in range(N):
            dp[i][i] = True

        for i in range(N-1):
            dp[i][i+1] = s[i] == s[i+1]

        length = 2
        max_length = 1

        while length < N:
            start = 0
            while start + length < N:
                if dp[start+1][start+length-1] and s[start] == s[start+length]:
                    dp[start][start+length] = True
                    max_length = max(max_length, length)
                start += 1
            length += 1
        return max_length

    # Notice
    # 1. dp[i][j] means if s[i:j] is a palindrome
    # 2. dp[i][i] = True
    #    dp[i][i+1] = True if s[i] == s[i+1]
    # 3. dp[start][start+length] = True if s[start] == s[star+length] and dp[start+1][start+length-1]
    # 4. Update length
    # This dp way is O(n^2) will get TLE
    """
    Other Ways
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
        st = (ansp - p[ansp] + 1) / 2
        return s[st:st + p[ansp] - 1]
    """
