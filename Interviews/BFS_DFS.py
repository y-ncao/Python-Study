"""
#####Summarize all kind of ways to do Tree Traversal
* BFS
  * Level Order Traversal(Use double loop)
* DFS
  * Preorder(Recursive, Iterative)
  * Inorder(Recursive, Iterative)
  * Postorder(Recursive, Iterative)
"""

def BFS_level_order_traversal(root):
    if not root:
        return
    queue = [root]
    ret = []
    while len(queue) > 0:
        size = len(queue)
        level = []
        for i in range(size):
            node = queue.pop()
            level.append(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        ret.append(level[:])
    return ret

# First all recursive
def DFS_preorder(root):
    if not root:
        return
    print root.val
    DFS_preorder(root.left)
    DFS_preorder(root.right)

# Use stack
def DFS_perorder(root):
    if not root:
        return
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        print node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Divde and Conquer
# Not sure how this gonna work
def DFS_preorder(root):
    if not root:
        return []

    left  = DFS_preorder(root.left)
    right = DFS_preorder(root.right)

    result.append(root.val)
    result.extend(left)
    result.extend(right)
    return result

# Recursive
def DFS_postorder(root):
    if not root:
        return
    DFS_postorder(root.left)
    DFS_postorder(root.right)
    print root.val

# Divide and Conquer
def DFS_postorder(root):
    if not root:
        return []

    left = DFS_postorder(root.left)
    right = DFS_postorder(root.right)

    result.extend(left)
    result.extend(right)
    result.append(root.val)             # ?WTF just switch the place?
    return result

# Use stack
def DFS_postorder(root):
    if not root:
        return []
    res = []
    stack = [root]
    prev = None

    while len(stack) > 0:
        node = stack.pop()
        if prev is None or prev.left == node or prev.right == node: # Traverse down the tree
            if node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)
        elif node.left == prev:
            stack.append(node.right)
        else:
            res.append(node.val)
            stack.pop()
        prev = node
    return res
