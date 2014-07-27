"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    def minDepth(self, root):
        return self.minDepth_rec(root)

    def minDepth_rec(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth_rec(root.right) + 1
        if root.right is None:
            return self.minDepth_rec(root.left) + 1
        return min(self.minDepth_rec(root.left), self.minDepth_rec(root.right)) + 1

    # Must do it in this way.
    # It's different from the maxDepth because in max, we search for max
    # In this min, the min depth is root to leaf node
    # A leaf node is node does not have any child.
    # Those has one child cannot be called leaf node

    def minDepth_iter(self, root):
        if root is None:
            return 0
        queue = []
        queue.append( (root, 1) )
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append( (node.left, depth+1) )
            if node.right is not None:
                queue.append( (node.right, depth+1) )
