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

# Recursive Ways
def DFS_preorder(root):
    if not root:
        return
    print root.val
    DFS_preorder(root.left)
    DFS_preorder(root.right)

def DFS_inorder(root):
    if not root:
        return
    DFS_inorder(root.left)
    print root.val
    DFS_inorder(root.right)

def DFS_postorder(root):
    if not root:
        return
    DFS_postorder(root.left)
    DFS_postorder(root.right)
    print root.val


# Iterative Ways

# push right first then left
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

# if no left, move to right
def DFS_inorder(root):
    if not root:
        return
    stack = []
    cur = root
    while True:
        while cur:
            stack.append(cur)
            cur = cur.left
        if not stack:
            break
        cur = stack.pop()
        print cur
        cur = cur.right

# reverse the reversed preorder
def DFS_postorder(root):
    if not root:
        return
    stack = []
    ret = []
    while len(stack) > 0:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    print ret[::-1]


# Divde and Conquer
def DFS_preorder(root):
    if not root:
        return []

    left  = DFS_preorder(root.left)
    right = DFS_preorder(root.right)

    result.append(root.val)
    result.extend(left)
    result.extend(right)
    return result


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
