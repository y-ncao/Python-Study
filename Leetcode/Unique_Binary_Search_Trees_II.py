"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        nums = [ i for i in range(1, n+1)]
        return self.generateTrees_helper(nums)

    def generateTrees_helper(self, nums):
        if not nums:
            return [None]
        res = []
        for i, num in enumerate(nums):
            left = self.generateTrees_helper(nums[:i])
            right = self.generateTrees_helper(nums[i+1:])
            for l in left:
                for r in right:
                    root = TreeNode(num)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

    # Annie's DP way couldn't understand
