"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    def rotateRight(self, head, k):
        if not head:
            return None
        length = 1
        tail = head                     # Naming
        while tail.next:                # No need to use extra prev
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head                 # Detail
        tail.next = head
        cur = head
        i = 0
        while i < length - k - 1:       # Note this detail
            cur = cur.next
            i += 1
        new_head = cur.next
        cur.next = None
        return new_head
