"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:                # No need to check if head has only 1 or 2 nodes
            return None
        mid = head
        end = head
        prev = None
        while end.next is not None and end.next.next is not None:
            prev = mid                  # Very good way to keep record of last
            mid = mid.next
            end = end.next.next         # Doesn't matter what fast is, so no need to push to end
        if head == mid:
            head = None                 # This will ensure that we wouldn't create dup node to the left child
        if prev is not None:
            prev.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    # Important thing here:
    # Actually we only care about the mid of the Node
    # Annie is using pre-order traversal way, which is different.
