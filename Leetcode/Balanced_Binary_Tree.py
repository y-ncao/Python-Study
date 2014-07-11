"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.isBalanced_1(root)

    def isBalanced_1(self, root):
        if root is None:
            return True
        if self.get_height(root) == -1:
            return False
        return True

    def get_height(self, root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def isBalanced_2(self, root):
        if root is None:
            return True
        if abs(self.get_max_height(root.left) - self.get_max_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_max_height(self, root):
        if root is None:
            return 0
        return max(self.get_max_height(root.left), self.get_max_height(root.right)) + 1

    # First way is a little bit hard to think
    # Using -1 as return to sign if height diff > 1
    # First way has better performance
