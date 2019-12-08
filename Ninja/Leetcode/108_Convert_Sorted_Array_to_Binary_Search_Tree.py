"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        return self.sortedArrayToBSTRec(num, 0, len(num)-1)

    def sortedArrayToBSTRec(self, num, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(num[mid])
        node.left = self.sortedArrayToBstRec(num, start, mid-1)
        node.right = self.sortedArrayToBstRec(num, mid+1, end)
        return node
