#!/usr/bin/env python

# This is the structure of Node
# Note: there's no need to delare it before the __init__
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(current, data_list):
    if isinstance(current, int):
        current = Node(current)
    for data in data_list:
        new_node = Node(data)
        current.next = new_node
        current = new_node

def print_list(head):
    while head is not None:
        print head.data
        head = head.next

def append_to_tail(head, data):
    if head is None:
        return Node(data)
    current = head
    while current.next != None:
        current = current.next
    current.next = Node(data)
    return head

def append_to_head(head, data):
    new_head = Node(data)
    if head is not None:
        new_head.next = head
    return new_head

def delete_node(head, data):
    while head is not None and head.data == data:
        head = head.next
    prev = head
    current = head.next
    while current is not None:
        if current.data == data:
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next
    return head

def remove_duplicate(head):
    data_list = [head.data,]
    prev = head
    head = head.next
    while head is not None:
        # Found duplicate, delete it
        if head.data in data_list:
            prev.next = head.next
            head = head.next
        # Not found, keep go on
        else:
            data_list.append(head.data)
            head = head.next
            prev = prev.next

def find_kth(head, k):
    current = head
    for i in range(k):
        current = current.next
    while current is not None:
        head = head.next
        current = current.next
    return head.data

def delete_middle_node(node):
    if node is None or node.next is None:
        return False
    node.data = node.next.data
    node.next = node.next.next
    return True

def partition_list(head, x):
    before_head = None
    end_head    = None
    before_list = None
    after_lsit  = None
    while head is not None:
        if head.data <= x:
            if before_list is None:
                before_list = head
                before_head = head
            else:
                before_list.next = head
                before_list = before_list.next
        else:
            if end_list is None:
                end_list = head
                end_head = head
            else:
                end_list.next = head
                end_list = end_list.next
        head = head.next

    if before_head is None:
        return end_head

    before_list.next = end_head
    return before_head

def number_add(head1, head2):
    carry = 0
    prev = None
    head = None
    while head1 is not None or head2 is not None or carry>0:
        result = Node(0)
        if head is None:
            head = result
        if prev is not None:
            prev.next = result
        if head1 is not None and head2 is not None:
            result.data = (head1.data + head2.data + carry) % 10
            carry = (head1.data + head2.data + carry) / 10
            head1 = head1.next
            head2 = head2.next
        elif head1 is None and head2 is not None:
            result.data = (head2.data + carry) % 10
            carry = (head2.data + carry) / 10
            head2 = head2.next
        elif head2 is None and head1 is not None:
            result.data = (head1.data + carry) % 10
            carry = (head1.data + carry) / 10
            head1 = head1.next
        else:
            result.data = carry
            carry = 0
        prev = result
    return head

# This one need to confirm wether two lists have the same digits
"""
I'll come back later when I really want to do this stupid thing
def reverse_add(head1, head2):
    carry = 0
    prev = None
    while
"""

def find_begin_loop(head):
    slow_runner = head
    fast_runner = head

    while slow_runner != fast_runner:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

    # Met
    fast_runner = head
    while slow_runner != fast_runner:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next

    return slow_runner

# Later on check Palindom algorithm, pretty stupid in my memory

if __name__ == "__main__":
    a = Node(10)
    create_linked_list(a, [1,3,3,2,44,5,87,42,42])
    print '*'*10
    print_list(a)
    print '*'*10
    append_to_tail(a, 33)
    print '*'*10
    new_head = append_to_head(a,19)
    print_list(new_head)
    print '*'*10,'original'
    print_list(a)
    print '*'*10,'delete'
    print_list(delete_node(a,10))
    print '*'*10,'remove duplicate'
    remove_duplicate(a)
    print_list(a)
    print '*'*10
    print find_kth(a,1)
    print '*'*10
    head1 = Node(1)
    head2 = Node(2)

    create_linked_list(head1, [6,4,])
    print '*'*10
    create_linked_list(head2, [3,8,])

    print_list(head1)
    print '*'*10
    print_list(head2)
    print '*'*10
    print_list(number_add(head1,head2))
