"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        dummy = ListNode(-9223372036854775807-1)
        dummy.next = head
        cur = dummy
        while cur.next is not None:
            if cur.val < cur.next.val:
                cur = cur.next
            else:
                insert = cur.next
                cur.next = insert.next
                start = dummy
                while start.val < insert.val:
                    prev = start
                    start = start.next
                prev.next = insert
                insert.next = start
        return dummy.next

    # Write everything in one func MAY increase the speed of processing
    # Made a mistake here, pasted the code to Sort List and coulnd't pass...
    # 1. The insertion sort shown in wiki, will check from back to front. It's the same to check from front-back
