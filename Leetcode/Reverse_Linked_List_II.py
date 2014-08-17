"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        i = 1
        while i < m:
            start = start.next
            i += 1
        cur = start.next
        while i < n:
            move = cur.next
            cur.next = move.next
            move.next = start.next
            start.next = move
            i += 1
        return dummy.next
    # Can use or without dummy
