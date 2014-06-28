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



def copy_tree(root, new_node):
    if root.left is not None:
        new_node.left = tree_node(root.left.data)
        copy_tree(root.left, new_node.left)
    if root.right is not None:
        new_node.right = tree_node(root.right.data)
        copy_tree(root.right, new_node.right)
        
    return new_node
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

def covers(root, p):
    if root is None:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)

# store the result of cover so that we don't need to calculate it again
def first_common_ancestor(root, p, q):
    # p q not a child of root
    if not (covers(root, p) and covers(root,q)):
        return None
    p_is_left = covers(root.left, p)
    q_is_left = covers(root.left, p)
    # Diff sides
    if p_is_left != q_is_left:
        return root
    elif p_is_left:
        return first_common_ancestor(root.left, p, q)
    else:
        return first_common_ancestor(root.right, p, q)
        
def is_subtree(t1, t2):
    if t1 == None:
        return False
    
    if t1.data == t2.data:
        if is_match(t1, t2):
            return True

    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

def is_match(t1,t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    else:
        if t1.data != t2.data:
            return False
        else:
            return is_match(t1.left, t2.left) and is_match(t1.right, t2.right)

def print_path(node, path_list):
    path_list.append(node)

    if node.left is None and node.right is None:
        s = ''
        for key in path_list:
            s += str(key.data) + ' '
        print s
        return
    if node.left is not None:
        print_path(node.left, path_list)
        path_list.pop()

    if node.right is not None:
        print_path(node.right, path_list)
        path_list.pop()

def is_full(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None or root.right is None:
        return False
    return is_full(root.left) && is_full(root.right)

def is_complete(root):
    queue = deque([root,])
    empty = False
    while len(queue) > 0:
        n = queue.popleft()
        
        if n.left is None:
            empty = True
        else:
            if empty:
                return False
            queue.append(n.left)
        
        if n.right is None:
            empty = True
        else:
            if empty:
                return False
            queue.append(n.right)
    return True

def is_symmetry(n1, n2):
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None:
        return False
    if n1.data != n2.data:
        return False
    return is_symmetry(n1.left, n2.right) and is_symmetry(n1.right, n2.left)

def is_symmetry(root):
    if root is None:
        return True
    return is_symmetry(root.left, root.right)

def mirrow_tree(root):
    if root is None:
        return
    mirrow_tree(root.left, root.left)

# Consider the case that t1 is None and T2 is not
def mirrow_tree(n1, n2):
    if n1 is None or n2 is None:
        return
    tmp = n1.data
    n1.data = n2.data
    n2.data = tmp
    if n1.left is not None and n2.right is not None:
        mirrow_tree(n1.left, n2.right)
    if n1.right is not None and n2.left is not None:
        mirrow_tree(n1.right, n2.left)
    # Not going to add more to here. Just add four more check here

# BFS way
def create_list_level_tree(root):
    result = [[root,],]
    prev = [root,]
    current = []
    while len(prev) > 0:
        for tree_node in prev:
            if tree_node.left is not None:
                current.append(tree_node.left)
            if tree_node.right is not None:
                current.append(tree_node.right)
        result.append(current)
        prev = current
        current = []

    return result

# DFS way

def create_list_level_tree(root):
    pass

# Check if a BT is a BST, use in-order traverse and copy to a list
def check_bst(root):
    bst_list = []
    def copy_bst(root):
        if root is None:
            return
        copy_bst(root.left)
        bst_list.append(root)
        copy_bst(root.right)
    prev = bst_list[0]
    for node in bst_list[1:]:
        if prev.data >= node.data:
            return False
        else:
            prev = node
    return True

# Use a left node < current < right node
def check_bst(root, min_value, max_value):
    if root is None:
        return True
    if root.data < min_value or root.data > max_value:
        return False

    if not check_bst(root.left, min_value, root.data) or not check_bst(root.right, root.data, max_value):
        return False

    return True


def get_rank(root, num):
    pass

def tree_diameter(root, num):
    pass

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
    #print '\nCopy Tree'
    print '\nPrint Path'
    path_list = []
    print_path(root, path_list)
