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
        if head is None:
            return None
        dummy = ListNode(0)
        cur = dummy
        while head.next is not None:
            if head.val == head.next.val:
                #jump here, need to find next start
                dup = head
                while head is not None and head.val == dup.val:
                    head = head.next
                # Stop if head it None or found a new head val
                if head is None:
                    break
            else:
                cur.next = head
                cur = cur.next
                head = head.next
                cur.next = None         # Clean up the last pointer

        if head is not None:            # Process the last one
            cur.next = head
        return dummy.next
