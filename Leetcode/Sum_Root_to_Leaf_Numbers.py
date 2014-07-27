"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
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
    def sumNumbers(self, root):
        return self.sumNumbers_2(root)

    def sumNumbers_1(self, root):
        if root is None:
            return 0
        ret = [0]
        self.sumNumbers_helper(root, 0, ret)
        return ret[0]

    def sumNumbers_helper(self, root, res, ret):
        res = res * 10 + root.val
        if root.left is None and root.right is None: # Found a leaf node
            ret[0] += res
            return
        if root.left is not None:
            self.sumNumbers_helper(root.left, res, ret)
        if root.right is not None:
            self.sumNumbers_helper(root.right, res, ret)

    # Miracle to do this in one submit
    # Now think about a way to do this without using list[0]

    # Second way but this will reduce the check of root.left is None or root.right is None
    def sumNumbers_2(self, root):
        ret = [0]
        self.sumNumbers_2_helper(root, 0, ret)
        return ret[0]

    def sumNumbers_2_helper(self, root, res, ret):
        if root is None:
            return
        res = root.val + res * 10
        if root.left is None and root.right is None:
            ret[0] += res
            return
        self.sumNumbers_2_helper(root.left, res, ret)
        self.sumNumbers_2_helper(root.right, res, ret)
