"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        next_node = mid.next
        mid.next = None
        first_half = self.sortList(head)
        second_half = self.sortList(next_node)
        return self.merge_list(first_half, second_half)

    def merge_list(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

    def find_mid(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Way to think about this:
    # 1. Split the list into first half and second half
    # 2. Recursion sort the two half
    # 3. Merge those two
