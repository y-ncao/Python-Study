#!/usr/bin/env python

# This is the structure of TreeNode
class TreeNode:
    left, right, data = None, None, None

    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

# Methods to play around with Tree
"""
# Need to look back what's wrong with my implementation
def insert_node(current_node, new_node):
    if isinstance(new_node, int):
        new_node = TreeNode(new_node)
    if current_node.data < new_node.data:
        if current_node.right is None:
            current_node.right = new_node
            return
        insert_node(current_node.right, new_node)
    else:
        if current_node.left is None:
            return
        insert_node(current_node.left, new_node)
"""
def insert_node(current_node, data):
    if not isinstance(current_node, TreeNode):
        current_node = TreeNode(data)
    else:
        if current_node.data > data:
            current_node.left = insert_node(current_node.left, data)
        else:
            current_node.right = insert_node(current_node.right, data)

    return current_node

def insert_list(root, list):
    for data in list:
        insert_node(root, data)

def print_tree(tree_node):
    if tree_node is None:
        return
    else:
        print tree_node.data
        print_tree(tree_node.left)
        print_tree(tree_node.right)

def is_empty(tree_node):
    if isinstance(tree_node, TreeNode):
        return False
    else:
        return True

def find_min(tree_node):
    if tree_node.left is None:
        return tree_node.data
    else:
        return find_min(tree_node.left)

def find_max(tree_node):
    if tree_node.right is None:
        return tree_node.data
    else:
        return find_max(tree_node.right)

def get_height(tree_node):
    if tree_node is None:
        return 0
    else:
        return max(get_height(tree_node.left), get_height(tree_node.right)) + 1

def is_balance(tree_node):
    if tree_node is None:
        return True
    if abs(get_height(tree_node.left)-get_height(tree_node.right)) > 1:
        return False
    else:
        return is_balance(tree_node.left) and is_balance(tree_node.right)

if __name__ == "__main__":
    root = TreeNode(19)
    insert_list(root, [3,6,9,18,20,21,25])
    print_tree(root)
    print is_empty(root)

    print 'max and min'
    print find_min(root)
    print find_max(root)

    print 'Height'
    print get_height(root)

    print 'Balanced'
    print is_balance(root)
    print 'testing'
    print root.left.data
