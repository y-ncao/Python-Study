"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
        nodes = []
        for i in range(n):
            nodes.append(n+1)
        res = 0
        numTreeHelper(res, nodes)
        return res

    def numTreeHelper(self, res, nodes):
        N = len(nodes)
        if N <= 1:
            return N
        for i in range(N):
            res += numTreeHelper(nodes[:i]) * numTreeHelper(nodes[i+1:])
