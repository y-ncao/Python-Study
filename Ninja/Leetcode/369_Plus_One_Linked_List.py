"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast:
            if fast.val != 9:
                slow = fast
            fast = fast.next

        slow.val += 1
        slow = slow.next
        while slow:
            slow.val = 0
            slow = slow.next

        return dummy.next if dummy.val == 0 else dummy
