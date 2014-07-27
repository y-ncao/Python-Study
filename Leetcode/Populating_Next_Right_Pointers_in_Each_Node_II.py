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
        if root is None:
            return
        if root.left is not None:
            if root.right is not None:
                root.left.next = root.right
            else:
                root.left.next = self.find_next(root.next)

        if root.right is not None:
            root.right.next = self.find_next(root.next)

        self.connect(root.right)        # Do right first then left
        self.connect(root.left)

    def find_next(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return self.find_next(root.next)
        if root.left is not None:
            return root.left
        return root.right

    # This is miracle that I can do this with one time!!!!
    # Very simple to think
    # One thing need to notice is that need to do connect right first and then left
    # Because otherwise, when linking towards the right but the right isnt ready there will be error
