"""
#####From [blog](http://blog.csdn.net/luckyxiaoqiang/article/details/7518888#topic6)

Not sure if this is usefull but the code seems pretty important
"""

def get_kth_level_nodes(root, k):
    if not root:
        return 0
    if k == 1:
        return k

    left_count = get_kth_level_nodes(root.left, k-1)
    right_count = get_kth_level_nodes(root.right, k-1)

    return left_count + right_count

"""
from Tree_Helper.tree_helper import *
A = [ i for i in range(20)]
root = create_bst_from_array(A)

DFS_level_order_traversal(root)

print get_kth_level_nodes(root, 5)
"""
