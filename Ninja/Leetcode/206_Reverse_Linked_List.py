"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # This is the moving head pointer solution
        if not head:
            return None

        next = None
        new_head = head
        while head.next:
            next = head.next
            head.next = next.next
            next.next = new_head
            new_head = next
        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        # This is the double pointer solution
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev
