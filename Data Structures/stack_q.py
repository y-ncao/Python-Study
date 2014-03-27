#!/usr/bin/env python

# This is the structure of Node

class Node:
    data = None
    next = None
    def __init__(self, data):
        self.data = data
        self.next = None

def append_to_head(node, data):
    head = Node(data)

    if node is not None:
        head.next = node

    return head

def append_to_tail(node, data):
    tail = Node(data)

    if node is None:
        return tail
    else:
        head = node
        while node.next is not None:
            node = node.next
        node.next = tail
        return head

# Check back later
def delete(head, data):
    if head.data == data:
        head = head.next
    previous = head
    while node is not None:
        if node.data == data:
            previous.next= node.next
            node = node.next
        else:
            previous = previous.next
            node = node.net

    return head
