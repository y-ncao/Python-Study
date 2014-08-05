"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        ret = []
        if root is None:
            return ret
        queue = [root, None]
        res = []
        zig = False                     # Because we start from very root, so no reverse at that point
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                if zig:
                    ret.append(res[::-1])
                else:
                    ret.append(res[:])
                res = []
                if len(queue) == 0:
                    break
                zig = not zig
                queue.append(None)
            else:
                res.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return ret
