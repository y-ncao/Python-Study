"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root or (not root.left and not root.right):
            return
        if root.left and root.right:
            root.left.next = root.right

        next_node = self.find_next(root.next)
        if root.right:
            root.right.next = next_node
        else:
            root.left.next = next_node

        self.connect(root.right)        # Do right first then left
        self.connect(root.left)

    def find_next(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return self.find_next(root.next)
        if root.left:
            return root.left
        else:
            return root.right
    # Notice:
    # 1. Note that line 47 need to do right first then left
    # 2. The reason that I doesn't need to process I first is it doesn't need to process
    #    nodes of root.next.next...
