#!/usr/bin/env python
class tree_node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_minimum_BST(data_list, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    n = tree_node(data_list[mid])
    n.left = create_minimum_BST(data_list, start, mid-1)
    n.right = create_minimum_BST(data_list, mid+1, end)
    return n

def in_order_traverse(root):
    if root is None:
        return
    in_order_traverse(root.left)
    print root.data
    in_order_traverse(root.right)

def pre_order_traverse(root):
    if root is None:
        return
    print root.data
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)

def post_order_traverse(root):
    if root is None:
        return
    post_order_traverse(root.left)
    post_order_traverse(root.right)
    print root.data

def dfs(root):
    if root is None:
        return
    stack = [root,]
    while len(stack) > 0:
        node = stack.pop()
        print node.data
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

from collections import deque

def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        print node.data
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

# Note:
# inorder preorder postorder are all DFS
# if you want to implement inorder, you need to first push right to stack since stack is LIFO
# but in BFS, just use normal left -> right would be fine

def get_height(root):
    if root is None:
        return 0

    return max( get_height(root.left), get_height(root.right)) + 1

def is_balance(root):
    if root is None:
        return True
    if abs(get_height(root.left) - get_height(root.right)) > 1:
        return False
    return is_balance(root.left) and is_balance(root.right)

if __name__ == '__main__':
    data_list = [1,3,4,5,6,8,9,10,13,14,17,18]
    root = create_minimum_BST(data_list, 0, len(data_list)-1)
    print root.data,root.left.data,root.right.data
    print '\nIn Order Traverse'
    in_order_traverse(root)
    print '\nPre Order Traverse'
    pre_order_traverse(root)
    print '\Post Order Traverse'
    post_order_traverse(root)
    print '\nDFS'
    dfs(root)
    print '\nBFS'
    bfs(root)
