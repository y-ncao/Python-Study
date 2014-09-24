"""
###9/23/2014 Interview with Kevin from Fivestars

safes = [2, 5, 4, 10, 7, 2, 6, 8, 1, 10]
            x      x     x     x     x

Given an array of numbers, choose the numbers that cannot become neighbor to each other, find out the largest sum

Note:
1. First attempt use greedy search, I think the reasult fails
2. Second attemp use dp, but a little bit hard to find out the transfer function, here's the coding
"""

def find_largest_none_close_sum(A):
    N = len(A)
    dp = [ 0 for i in range(N)]

    for i in range(N):
        if i == 0:
            dp[i] = A[0]
        elif i == 1:
            dp[i] = max(A[0], A[1])
        else:
            dp[i] = max(dp[i-2] + A[i], dp[i-1])

    return dp[N-1]

# 1. dp[i] means from 0 ... i the max sum none closing numbers
# 2. dp[0] = A[0], dp[1] = max(A[0], A[1])
# 3. dp[i] = dp[i] = max(dp[i-2] + A[i], dp[i-1])
# 4. dp[N-1]
