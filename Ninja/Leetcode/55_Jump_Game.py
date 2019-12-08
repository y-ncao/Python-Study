"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        return self.canJump_1(A)

    # Real DP way, but TLE. This is a O(n^2)'s solution
    def canJump_3(self, A):
        if A[0] == 0:
            return False
        N = len(A)
        dp = [False for i in range(N)]
        dp[0] = True
        for i in range(1, N):
            for j in range(i)[::-1]:
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
        return dp[N-1]
    # Note:
    # 1. dp[i] means whether we can jump to i
    # 2. dp[0] = True
    # 3. dp[i] = True if from i-1 ... 0 if we can jump to i
    # 4. dp[N-1]

    # Constant DP
    def canJump_1(self, A):
        pre_max = A[0]
        for i in range(1, len(A)):
            max_jump = max(pre_max-1, A[i-1]-1)
            if max_jump < 0:            # Note this is < 0 but not <= 0
                return False
            pre_max = max_jump
        return True

    # Another DP
    def canJump_2(self, A):
        dp = [0 for i in range(len(A))]
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = max(dp[i-1]-1, A[i-1]-1)
            if dp[i] < 0:
                return False
        return True
    # Note:
    # 1. dp[i] means at i, we can jump to where
    # 2. dp[0] = A[0]
    # 3. dp[i] = max(A[i-1]-1, dp[i-1]-1), if dp[i] < 0: then return False
    # return True if we can finish the loop
