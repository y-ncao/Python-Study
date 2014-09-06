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
        queue = [root, ]
        while len(queue)>0:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop()
                level.append(node.val)
                if node.left is not None:
                    queue.insert(0, node.left)
                if node.right is not None:
                    queue.insert(0, node.right)
            res.append(level[:])
        return res

    # Note
    # 1. Try to use double loop to do this
    # 2. Other ways are: a. use dummy node(None) b. use two queues
