"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

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
    def preorderTraversal(self, root):
        return self.preorderTraversal_1(root)

    def preorderTraversal_1(self, root):
        stack = []
        current = root
        res = []
        while current is not None or len(stack)>0:
            if current is not None:
                res.append(current.val)
                stack.append(current)
                current = current.left
            elif len(stack)>0:
                current = stack.pop()
                current = current.right
        return res

    def preorderTraversal_2(self, root):
        res = []
        self.preorderTraversal_rec(root, res)
        return res

    def preorderTraversal_rec(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.preorderTraversal_rec(root.left, res)
        self.preorderTraversal_rec(root.right, res)
