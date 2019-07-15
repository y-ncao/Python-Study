class TreeNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

class LinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def binary_search(root_node, target):
    while(root_node.left or root_node.right):
        if root_node.data == target:
            return True
        elif root_node.data < target:
            root_node = root_node.right
        else:
            root_node = root_node.left
    return False

def binary_search(search_list, target):
    left_index = 0
    right_index = len(list) - 1
    while left_index < right_index:
        mid = (left_index + right_index) / 2
        if target == search_list[mid]:
            return True
        elif target < search_list[mid]:
            right_index = mid - 1
        else:
            left_index = mid + 1

    return False

def bfs(tree_node, target):
    q = []
    q.append(tree_node)
    while q:
        current = q.popleft()
        if not current:
            continue
        if current.data == target:
            return True
        q.append(current.left)
        q.append(current.right)
    return False

def permute(self, n):
    self.result = []
    self.permute_helper([], n)
    return self.result

def permute_helper(self, current_result, n):
    if len(current_result) == n:
        self.result.append(current_result)
        return

    cannot_permute_R = len(current_result) >= 2 and current_result[-1] == current_result[-2] == 'R'
    cannot_permute_B = len(current_result) >= 2 and current_result[-1] == current_result[-2] == 'B'

    if not cannot_permute_R:
        self.permute_helper(current_result + ['R'], n)

    if not cannot_permute_B:
        self.permute_helper(current_result + ['B'], n)
