"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        max_profit = 0
        low_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - low_price)
            low_price = min(low_price, price)
        return max_profit
