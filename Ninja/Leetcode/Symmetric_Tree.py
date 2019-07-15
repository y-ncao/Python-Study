"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        return self.isSymmetric_2(root)

    def isSymmetric_1(self, root):
        if root is None:
            return True
        return self.symmetric_helper(root.left, root.right)

    def symmetric_helper(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2 or n1.val != n2.val:
            return False
        return self.symmetric_helper(n1.left, n2.right) and self.symmetric_helper(n1.right, n2.left)

    # No need to use two queues here, just one but pop twice would be fine
    # Keep in mind which node should be pop first
    def isSymmetric_2(self, root):
        if root is None:
            return True
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while len(queue)>0:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None or t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
