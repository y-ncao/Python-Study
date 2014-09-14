"""
#####NC Class 5, slides 17

The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

[Solution](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)

1. dp[i] is length of LIS ends with char i
2. dp[0...N] = 1
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
    sequence = []
    for i in range(N)[::-1]:
        if dp[i] != max_len:
            continue
        else:
            sequence.insert(0, A[i])
            max_len -= 1
    print sequence
    return max_len

A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print LIS(A)

# Using this can print one answer
# if need to print all, would rather do a dfs

def LIS(A):
    ret = {}
    LIS_helper(A, [], ret)
    return ret

def LIS_helper(A, res, ret):
    if not A:
        ret.setdefault(len(res[:]), []).append(res[:])
        return
    for i, num in enumerate(A):
        if not res or num > res[-1]:
            res.append(num)
            LIS_helper(A[i+1:], res, ret)
            res.pop()
A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
d_A = LIS(A)

print d_A[max(d_A.keys())]
