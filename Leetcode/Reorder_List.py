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
        if head is None or head.next is None:
            return
        slow = head
        fast = head.next.next                     # Let fast go one more round first then we don't need mid
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        mid = slow
        cur = mid.next
        while cur.next is not None:
            move = cur.next
            cur.next = move.next
            move.next = mid.next
            mid.next = move
        left = head                     # Start to merge two lists
        while left != mid:              # Ends when left = mid
            right = mid.next
            mid.next = right.next
            right.next = left.next
            left.next = right
            left = right.next

    # Way to think:
    # If we loop the list all the time, it will exceed the time limit
    # So just find the second half, reverse the second half, and merge it with the first half, that's done
    """This way should work, but will exceed the time limit
    def reorderList(self, head):
        while head is not None:
            tail = head
            prev = tail
            while tail.next is not None:
                prev = tail
                tail = tail.next
            if prev == tail:
                return
            prev.next = None
            tail.next = head.next
            head.next = tail
            head = tail.next
    """
