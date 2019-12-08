"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root
    # Only difference if pop(0) or pop()
    # In this case need to do right first
