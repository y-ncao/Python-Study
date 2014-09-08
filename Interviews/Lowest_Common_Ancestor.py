"""
#####[LCA, Lowest Common Ancestor](http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/)Pocket Gem possible question 9/8/2014

Use O(n)
"""

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
