"""
Given a linked list where every node represents a linked list and contains two pointers of its type:
(i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)
(ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).
All linked lists are sorted. See the following example
```
       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
```
"""

class Node():
    def __init__(self, data):
        self.right = None
        self.down = None
        self.data = data

def flatten(node):
    if not node or not node.right:
        return node

    return merge(node, flatten(node.right))

def merge(node1, node2):
    if not node1:
        return node2
    if not node2:
        return node1

    if node1.data < node2.data:
        head = node1
        head.next = merge(node1.next, node2)
    else:
        head = node2
        head.next = merge(node1, node2.next)
    return head

# Notice:
# This is very qiao miao. Using recursion is like DFS, so will first flatten from the end.
# When we want to flatten the front part, the back parts are already flattened
