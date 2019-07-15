"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

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
    def postorderTraversal(self, root):
        return self.postorderTraversal_1(root)

    # I prefer this way
    def postorderTraversal_1(self, root):
        if root is None:
            return []
        stack = [root]
        output = []
        while len(stack)>0:
            node = stack.pop()
            output.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return output[::-1]

    # I don't like this way
    def postorderTraversal_2(self, root):
        stack = []
        current = root
        res = []
        last = None
        while current is not None or len(stack)>0:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                peak = stack[-1]
                if peak.right is not None and last != peak.right:
                    current = peak.right
                else:
                    last = stack.pop()
                    res.append(last.val)
        return res

    def postorderTraversal_3(self, root):
        res = []
        self.postorderTraversal_rec(root, res)
        return res

    def postorderTraversal_rec(self, root, res):
        if root is None:
            return
        self.postorderTraversal_rec(root.left, res)
        self.postorderTraversal_rec(root.right, res)
        res.append(root.val)
