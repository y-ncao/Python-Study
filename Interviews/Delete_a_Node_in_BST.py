"""
[Solution](http://answer.ninechapter.com/solutions/delete-a-node-in-binary-search-tree/)
实际上有好几种做法
1. replace current node with left maximum node
2. replace current node with right minimum node
3. 整体移动，前提是这个node只能有一边的subtree

这里就直接选第一种作为解法
但是这种也有特殊情况
1. no left subtree (只有一边有子树，简单，直接挪大块)
2. left maximum has a left child (不管有没有，都得把left child分配给max_node_parent，但是left maximum一定没有right child)
3. node is root of the tree (use dummy node)

"""
def delete_node(root, val):
    dummy_node = treeNode(0)
    dummy_node.left = root
    find_delete(dummy_node, root)
    return dummy_node.left

def find_delete(parent, node, val):
    if node is None:
        return
    if node.val == val:
        delete_node_in_BST(parent, node)
    elif node.val < val:
        find_delete(node, node.right, val)
    else:
        find_delete(node, node.left, val)

def delete_node_in_BST(parent, node):
    if not node.left:
        if parent.left == node:
            parent.left = node.right
        else:
            parent.right = node.right
    else:
        max_node_parent = node
        max_node = node.left

        while max_node.right:
            max_node_parent = max_node
            max_node = max_node.right

        # Found max_node and max_node_parent, need to replace max_node_parent a new child
        # max_node won't have a right child
        if max_node_parent.left == max_node:
            max_node_parent.left = max_node.left
        else:
            max_node_parent.right = max_node.right

        # Move max_node to node
        max_node.left = node.left
        max_node.right = node.right
        if parent.left == node:
            parent.left = max_node
        else:
            parent.right = max_node
