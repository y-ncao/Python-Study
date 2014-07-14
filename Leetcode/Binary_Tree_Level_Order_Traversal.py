"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res = []
        if root is None:
            return res
        queue = []
        level = []
        queue.append(root)
        queue.append(None)
        while len(queue)>0:
            node = queue.pop(0)
            if node is None:
                res.append(level[:])
                level = []
                if len(queue)>0:
                    queue.append(None)
            else:
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return res
    # Found out why, the question want the val of the node but not the whole node
