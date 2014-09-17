"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    def minDepth(self, root):
        if not root:
            return 0
        return self.minDepth_rec(root)

    def minDepth_rec(self, root):
        if not root:
            return 9223372036854775807
        if root.left is None and root.right is None:
            return 1
        return min(self.minDepth_rec(root.left), self.minDepth_rec(root.right)) + 1
