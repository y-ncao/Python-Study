"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        pq = []
        for node in lists:
            if node is not None:
                heapq.heappush(pq, (node.val, node))
        dummy = ListNode(0)
        cur = dummy
        while len(pq) > 0:
            val, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next
            if node.next is not None:
                heapq.heappush(pq, (node.next.val, node.next))
        return dummy.next

    # Remember this to use Priority Queue
