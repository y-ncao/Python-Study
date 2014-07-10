"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        return self.climbStairs_2(n)

    def climbStairs_1(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs_2(self, n):
        if n <= 1:
            return n
        dp = [ 0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

    def climbStairs_3(self, n):
        if n <= 2:
            return n
        fn_1 = 1
        fn_2 = 2
        for i in range(3, n+1):
            fn = fn_1 + fn_2
            fn_1 = fn
            fn_2 = fn_1
        return fn
