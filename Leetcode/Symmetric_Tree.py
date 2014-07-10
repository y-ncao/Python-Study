"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.symmetric_helper(root.left, root.right)

    def symmetric_helper(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        if n1.val != n2.val:
            return False
        return self.symmetric_helper(n1.left, n2.right) and self.symmetric_helper(n1.right, n2.left)

    # This is accepted. Next is do it iteratively
