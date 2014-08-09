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
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        prev = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        head = self.sortList(head)
        slow = self.sortList(slow)
        return self.sortedMerge(head, slow)

    def sortedMerge(self, head1, head2):
        dummy = ListNode(0)
        head = dummy
        while head1 is not None or head2 is not None:
            if head1 is None:
                head.next = head2
                head2 = head2.next
            elif head2 is None:
                head.next = head1
                head1 = head1.next
            elif head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        return dummy.next

    # Way to think about this:
    # 1. Split the list into first half and second half
    # 2. Recursion sort the two half
    # 3. Merge those two
