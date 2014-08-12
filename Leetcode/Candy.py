"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        N = len(ratings)
        candy = [1 for i in range(N)]
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
        return sum(candy)
