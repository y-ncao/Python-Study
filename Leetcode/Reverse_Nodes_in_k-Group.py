"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head

        total_nodes = 0
        cur = head
        while cur is not None:
            cur = cur.next
            total_nodes += 1
        n = total_nodes / k

        prev = dummy
        while n > 0:
            i = 1
            cur = prev.next
            while i < k:
                move = cur.next
                cur.next = move.next
                move.next = prev.next
                prev.next = move
                i += 1
            prev = cur
            n -= 1
        return dummy.next
