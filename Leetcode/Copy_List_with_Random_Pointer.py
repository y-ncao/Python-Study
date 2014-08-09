"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        cur = head
        while cur is not None:
            newNode = RandomListNode(cur.label)
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode.next
        cur = head
        while cur is not None:
            newNode = cur.next
            if cur.random is not None:  # random pointer may not exist
                newNode.random = cur.random.next
            cur = newNode.next
        cur = head
        newNodehead = head.next
        while cur is not None:
            newNode = cur.next
            cur.next = newNode.next
            if newNode.next is not None:
                newNode.next = newNode.next.next
            cur = cur.next
        return newNodehead
