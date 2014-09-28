"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.last = None
        self.wrongs = [None, None]
        self.recover_helper(root)
        self.wrongs[0].val, self.wrongs[1].val = self.wrongs[1].val, self.wrongs[0].val
        return root

    def recover_helper(self, root):
        if not root:
            return
        self.recover_helper(root.left)
        if self.last and self.last.val > root.val:
            if not self.wrongs[0]:
                self.wrongs[0] = self.last
            self.wrongs[1] = root
        self.last = root

        self.recover_helper(root.right)

    # Note:
    # 1. Very normal inorder traversal
    # 2. Notice link 32,33. Always update wrongs[1], but wrongs[0] will only update one time
    #    Reason is:
    #    Imaging [1,2,3,4,5,6], swap to [1,2,6,4,5,3]
    #    We will find out 6 > 4 and 5 > 3
    #    So we first update wrongs[0] = last, then update wrongs[1] = root
