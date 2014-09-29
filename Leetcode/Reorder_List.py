"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        next_node = mid.next
        mid.next = None
        second_half = self.reverse(next_node)

        self.merge(head, second_half)
        return head

    def find_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        dummy = ListNode(0)
        dummy.next = head
        while head.next:
            move = head.next
            head.next = move.next
            move.next = dummy.next
            dummy.next = move
        return dummy.next

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        i = 0
        while l1 and l2:
            if i % 2 == 0:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            i += 1
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
