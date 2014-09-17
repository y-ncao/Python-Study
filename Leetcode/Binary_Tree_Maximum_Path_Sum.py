"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        self.max_sum = -9223372036854775808
        self.maxPathSum_helper(root, self.max_sum)
        return self.max_sum

    def maxPathSum_helper(self, root, max_sum):
        if root is None:
            return 0

        left = self.maxPathSum_helper(root.left, max_sum)
        right = self.maxPathSum_helper(root.right, max_sum)

        root_max = max(root.val, left + root.val, right + root.val)
        self.max_sum = max(self.max_sum, root_max, left + right + root.val)

        return root_max
