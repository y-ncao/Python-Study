#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def DFS_level_order_traversal(root):
    ret = {}
    DFS_helper(ret, 1, root)
    for level in sorted(ret.keys()):
        print ret[level]

def DFS_helper(ret, level, root):
    if not root:
        return

    ret.setdefault(level, []).append(root.val)
    DFS_helper(ret, level + 1, root.left)
    DFS_helper(ret, level + 1, root.right)

def create_bst_from_array(A, start=None, end=None):
    if start is None and end is None:
        start = 0
        end = len(A) - 1

    if start > end:
        return None

    mid = (start + end) / 2
    root = TreeNode(A[mid])

    root.left = create_bst_from_array(A, start, mid - 1)
    root.right = create_bst_from_array(A, mid + 1, end)

    return root

def print_tree_as_list(head):
    while head:
        print head.val,
        if head.left:
            print 'left', head.left.val,
        if head.right:
            print 'right', head.right.val,
        print ''
        head = head.right
