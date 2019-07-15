"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        N = len(prices)
        if N <= 1:
            return 0
        dp_1 = [0 for i in range(N)]
        dp_2 = [0 for i in range(N)]
        min_price = prices[0]
        i = 1
        while i < N:
            min_price = min(min_price, prices[i])
            dp_1[i] = max(dp_1[i-1], prices[i]-min_price)
            i+= 1

        max_price = prices[-1]
        i = N-2
        while i >= 0:
            max_price = max(max_price, prices[i])
            dp_2[i] = max(dp_2[i+1], max_price-prices[i])
            i -= 1
        res = 0
        for i in range(N):
            res = max(res, dp_1[i] + dp_2[i])
        return res
    # Very similart to trapping rain water, from left to right then right to left
