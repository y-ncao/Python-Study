"""
#####NC Class 5, slides 17

The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

1. dp means ends with char i, the length of LIS
2. dp[n] = 1
3. dp[i] = for j in range(i): if A[j] <= A[i], max(dp[i], dp[j]+1)
4. dp[N-1]
5. O(n^2)
"""

def LIS(A):
    N = len(A)
    dp = [1 for i in range(N)]
    max_len = 1
    for i in range(1, N):
        for j in range(i)[::-1]:
            if A[j] <= A[i]:
                dp[i] = max(dp[i], dp[j]+1)
                max_len = max(max_len, dp[i])
    return max_len

A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print LIS(A)
