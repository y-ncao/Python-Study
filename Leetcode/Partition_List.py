"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before_cur = before_dummy
        after_cur = after_dummy
        while head is not None:
            if head.val < x:
                before_cur.next = head
                before_cur = before_cur.next
                head = head.next
                before_cur.next = None
            else:
                after_cur.next = head
                after_cur = after_cur.next
                head = head.next
                after_cur.next = None
        if before_dummy.next is not None:
            before_cur.next = after_dummy.next
            return before_dummy.next
        else:
            return after_dummy.next
