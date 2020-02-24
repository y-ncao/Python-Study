"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast = slow = head
        while (
            fast and
            fast.next
        ):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

    # Remember to set slow = head.next and fast = head.next.next before entering the loop
    # Assume non-ring_length = a, ring_length = b, pointer fast went through f, pinter slow went through s.
    # So we know: f = 2s. f-s = nb
    # so s = nb. Which means short has went through n cycle's of the ring so far. So if we put f back to start, at the point they meet again, it's the entry point.
