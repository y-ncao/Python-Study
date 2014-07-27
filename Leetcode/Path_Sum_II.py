"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        ret = []
        self.pathSum_helper(root, sum, [], ret)
        return ret

    def pathSum_helper(self, root, sum, res, ret):
        if root is None:
            return
        if root.left is None and root.right is None:
            if sum == root.val:
                res.append(root.val)
                ret.append(res[:])
                res.pop()
            return
        res.append(root.val)
        self.pathSum_helper(root.left, sum - root.val, res, ret)
        self.pathSum_helper(root.right, sum - root.val, res, ret)
        res.pop()

"""
This way will have long run time
    def pathSum(self, root, sum):
        if root is None:
            return []
        ret = []
        self.pathSum_helper(root, sum, [root.val], ret)
        return ret

    def pathSum_helper(self, root, sum, res, ret):
        if root.left is None and root.right is None: # Found a leaf
            if sum == root.val:
                ret.append(res[:])
                return
        if root.left is not None:
            res.append(root.left)
            self.pathSum_helper(root.left, sum, res, ret)
            res.pop()
        if root.right is not None:
            res.append(root.right)
            self.pathSum_helper(root.right, sum, res, ret)
            res.pop()
"""
