"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head.next
        while cur:
            if prev.next.val != cur.val:
                prev = prev.next
                cur = cur.next
            else:
                while cur and cur.val == prev.next.val:
                    cur = cur.next
                prev.next = cur
                if cur:
                    cur = cur.next
        return dummy.next
    # Better way to do this
