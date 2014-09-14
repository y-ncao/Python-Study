"""
#####[LCA, Lowest Common Ancestor](http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/) Pocket Gem possible question 9/8/2014

Use O(n)
"""

# With Parent
def LCA(node1, node2):
    if node1 is None or node2 is None:
        return None
    path1 = get_path(node1)
    path2 = get_path(node2)

    index_1 = 0
    index_2 = 0
    while index_1 < len(path1) and index_2 < len(path2) and path1[index_1] == path2[index_2]:
        index1 += 1
        index2 += 1
    if index_1 < len(path1) and index_2 < len(path2):
        return path_1[index_1].parent
    else:
        return path_1[index_1 - 1]

    # Note:
    # 1. line 18 check if index is out of path:
    # if out of index: means node1/node2 is node2/node1's LCA, need to get index - 1
    # else:            we need to get parent

def get_path(node):
    path = []
    while node is not None:
        path.append(node)
        node = node.parent
    return path[::-1]

def get_path(root, node, current, path):
    if not root:
        return

    if root == node:
        path.append(current[:])
        return

    current.append(root)
    get_path(root.left, node, current, path)
    get_path(root.right, node, current, path)
    current.pop()

# Divdie and Conquer
def LCA(root, node1, node2):
    if not node1 or not node2:
        return None

    return get_LCA(root, node1, node2)

def get_LCA(root, node1, node2):
    if not root or node1 == root or node2 == root:
        return root

    left = get_LCA(root.left, node1, node2)
    right = get_LCA(root.right, node1, node2)

    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    return None
