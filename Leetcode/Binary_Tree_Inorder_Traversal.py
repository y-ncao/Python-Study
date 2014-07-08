"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        return self.inorderTraversal_1(root)

    def inorderTraversal_1(self, root):
        stack = []
        current = root
        res = []
        while current is not None or len(stack) > 0:
            if current is not None:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                current = stack.pop()
                res.append(current.val)
                current = current.right
        return res

    def inorderTraversal_2(self, root):
        res = []
        self.inorderTraversal_rec(root, res)
        return res

    def inorderTraversal_rec(self, root, res):
        if root is None:
            return
        self.inorderTraversal_rec(root.left)
        res.append(root.val)
        self.inorderTraversal_rec(root.right)
