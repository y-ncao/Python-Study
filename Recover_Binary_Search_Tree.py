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
        return self.recoverTree_2(root)

    # This is the first attempt, several things need to note
    # first and second need to be a list, so that it can work like pointer
    # Since we are only comparing the last and cur, we dont't need to store the whole list,
    # just use prev like solution 2
    # Be careful when doing the if/else check, we can use only if here like solution 2
    # Notice the way to determine the wrongs, always update the wrongs[1] but wrongs[0] will only updated once

    def recoverTree_1(self, root):
        nodes = []
        wrongs = [None, None]
        self.recoverTree_helper_1(root, nodes, wrongs)
        tmp = wrongs[0].val
        wrongs[0].val = wrongs[1].val
        wrongs[1].val = tmp
        return root

    def recoverTree_helper_1(self, root, nodes, wrongs):
        if root is None:
            return
        self.recoverTree_helper_1(root.left, nodes, wrongs)
        if len(nodes) == 0 or nodes[-1].val < root.val:
            pass
        else:
            if not wrongs[0]:
                wrongs[0] = nodes[-1]
            wrongs[1] = root
        nodes.append(root)
        self.recoverTree_helper_1(root.right, nodes, wrongs)

    # prev need to be a list inorder to use a pointer
    def recoverTree_2(self, root):
        wrongs = [None, None]
        self.recoverTree_helper_2(root, [None], wrongs)
        tmp = wrongs[0].val
        wrongs[0].val = wrongs[1].val
        wrongs[1].val = tmp
        return root

    def recoverTree_helper_2(self, root, prev, wrongs):
        if root is None:
            return
        self.recoverTree_helper_2(root.left, prev, wrongs)
        if prev[0] is not None and prev[0].val > root.val:
            if wrongs[0] is None:
                wrongs[0] = prev[0]
            wrongs[1] = root
        prev[0] = root
        self.recoverTree_helper_2(root.right, prev, wrongs)

"""
        if root is None:
            return None
        nodes = []
        queue = [root]
        while len(queue) > 0 and len(nodes)<=2:
            node = queue.pop()
            if node
"""
