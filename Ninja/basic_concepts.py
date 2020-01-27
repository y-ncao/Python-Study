## LinkedList, Double LinkedList. LinkedList Reverse
class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverse(self, head):
        prev = None
        while(head):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

class DLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    # Unconfirmed yet
    def reverse(self, head):
        prev = None
        while(head.next):
            temp = head.next
            head.next = prev
            if (prev):
                prev.prev = head
            prev = head
            head = tmp

## Tree and Tree Search
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeTraversal:
    def pre_order(self, root):
        if not root:
            return

        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if not root:
            return

        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)

    def post_order(self, root):
        if not root:
            return

        self.in_order(root.left)
        self.in_order(root.right)
        print(root.val)

    def binary_search_iteration(root, value):
        while(root.left and root.right):
            if root.val == value
                return True
            elif value < root.val:
                root = root.left
            else:
                root = root.right
        return False

    def binary_search_recursion(root, value):
        if not root:
            return False

        if root.val == value:
            return True
        elif value < root.val:
            return binary_search_recursion(root.left, value)
        else:
            return binary_search_recursion(root.right, value)

    def list_binary_search(search_list, target):
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

## Queue
queue = []  # same as list()
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0) # return 1
queue[0] # return 2 examine the first element

## Stack
stack = []
size = len(stack)
stack.append(1)
stack.append(2)
stack.pop() # return 2

## Priority Queue - https://docs.python.org/2/library/heapq.html
import heapq
heap = []
heapq.heappush(heap, 1)  # heap [1]
heapq.heappush(heap, 3)  # heap [1,3]
heapq.heappush(heap, 2)  # heap [1,3,2]
heapq.heappop(heap)  # 1
heapq.heappop(heap)  # 2
heapq.heappop(heap)  # 3

## Deque
import collections
dq = collections.deque()
dq.append(1)  # [1]
dq.appendleft(2)  # [2,1]
dq.popleft()  # [1]


## Set
s = set({1,3,4,5,6,5})  # {1, 3, 4, 5, 6}

## List
a = [5,4,3,2,1]
for index, value in enumerate(a):
    print(index, value)

## Dictionary
d.items()
d.keys()
d.values()


## Permutation
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
