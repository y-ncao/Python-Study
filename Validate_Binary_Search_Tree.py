"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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
    def isValidBST(self, root):
        return self.isValidBST_1(root)

    def isValidBST_1(self, root):         # sys.maxint and -sys.maxint-1
        return self.isValidBST_helper(root, -9223372036854775808,  9223372036854775807)

    def isValidBST_helper_1(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValidBST_helper_1(root.left, min, root.val) and self.isValidBST_helper_1(root.right, root.val, max)

    def isValidBST_2(self, root):
        return self.isValidBST_helper_2(root, -9223372036854775808)

    def isValidBST_helper_2(self, root, val):
        if root is None:
            return True
        if root.left is not None and not self.isValidBST_helper_2(root.left, val):
            return False
        if root.val <= val:
            return False
        val = root.val
        if root.right is not None and not self.isValidBST_helper_2(root.right, val):
            return False
        return True
