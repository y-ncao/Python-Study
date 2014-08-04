"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return None
        self.flatten_helper(root)

    def flatten_helper(self, root):
        if root.left is None and root.right is None:
            return root
        rhead = None                    # This declare is nessary
        if root.right is not None:
            rhead = self.flatten_helper(root.right)
        lend = root                     # Need this here
        if root.left is not None:
            lhead = self.flatten_helper(root.left)
            root.right = lhead
            lhead.left = None
            root.left = None
            while lend.right is not None: # Get the lend from root
                lend = lend.right

        if rhead is not None:
            lend.right = rhead
        return root
