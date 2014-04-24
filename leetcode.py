#!/usr/bin/env python

# 1.Single Number
# Fuck!!! use XOR
def single_number(num_list):
    for i in range(1, len(num_list)):
        if num_list[i] is not None:
            num_list[0] ^= num_list[i]

    return num_list[0]

# 2. Maximum depth of binary tree
def maximum_depth(root):
    if root is None:
        return 0

    return max( maximum_depth(root.left), maximum_depth(root.right)) + 1

# 3. Same Tree
def is_same_tree(p, q):
    # p q are both None so same
    if p is None and q is None:
        return True
    # one of the node is None but the other is not, not same
    elif p is None or q is None:
        return False
    # both of them are not None
    else:
        if p.data != q.data:
            return False
        else:
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# 4.Reverse Integer
def reverse_int(num):
    # Need to check negative, last digit zero
    is_nagative = 1
    if num < 0:
        is_nagative = -1
    digit_list = []
    num = abs(num)
    while num > 0:
        digit_list.append(num%10)
        num /= 10

    result = 0
    weight = len(digit_list)-1

    for digit in digit_list:
        result += digit * (10**weight)
        weight -= 1
    result *= is_nagative

    return result

# 5. Unique Binary Search tree
def unique_bst(num):
    if num <=1:
        return num

    return unique_bst_helper(1, num)

def unique_bst_helper(start, end):
    if start >= end:
        return 1

    result = 0
    for i in range(start, end+1):
        # sum the result on the left ande on the right
        result += unique_bst_helper(start, i-1) * unique_bst_helper(i+1, end)

    return result

# 6. Best time to buy and sell
def stock_buy_sell(stock_list):
    pre_price = stock_list[0]
    buy_price = stock_list[0]
    stock_empty = True
    profit = 0
    for i in range(1, len(stock_list)):
        # price decreasing, sell at previous point
        if stock_list[i] < pre_price:
            if stock_empty:
                # we got a lower buy price
                buy_price = stock_list[i]
            else:
                profit += pre_price - buy_price
                stock_empty = True
        # stock increasing, stock empty false
        else:
            stack_empty = False
        pre_price = stock_list[i]
    # last sell
    if not stock_empty:
        profit += pre_price - buy_price

# 7. Linked List Cycle
def list_cycle(head):
    slow = head
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast

# 8. BT Inorder traversal
def inorder_traversal(root):
    if root is None:
        return

    inorder_traversal(root.left)
    print root.data
    inorder_traversal(root.right)

# 9. BT Preorder traversal
def preorder_traversal(root):
    if root is None:
        return

    print root.data
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# 10. Populate Next right poiters in each node
def next_right_pointer(root):
    if root is None:
        return

    left = root.left
    right = root.right

    if left is not None and right is not None:
        left.next = right

    while left.right is not None:
        left = left.rigt
        right = right.left
        left.next = right

    next_right_pointer(root.left)
    next_right_pointer(root.right)

# 11. Search Insert Position
# This is a O(n) method, need to think about something for O(log(n))
def search_insert_position_1(num_list, num):
    i = 0
    while i <= len(num_list)-1:
        if num <= num_list[i]:
            return i
        i += 1
    return i

def search_insert_position(num_list, num, start, end):
    if start > end:
        return start

    mid = (start + end) / 2
    if num_list[mid] == num:
        return mid
    elif num_list[mid] > num:
        return search_insert_position(num_list, num, start, mid-1)
    else:
        return search_insert_position(num_list, num, mid+1, end)

# 12. Remove Duplicates from Sorted List:
def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    prev = head
    current = head.next
    while current is not None:
        if prev.data == current.data:
            prev.next = current.next
        else:
            prev = current
        currnet = current.next

    return head

# 13. Climbing Stairs
# Fuck you remember the num <= 2
def climb_stairs(num):
    if num <= 2:
        return num
    return climb_stairs(num-1) + climb_stairs(num-2)

# 14. Maximum Subarray
# important is the way to think this shit!!!
def maximum_subarray(array):
    sum = 0
    max = MIN_INT
    for i in range(0, len(array)):
        sum += array[i]
        if sum >= max:
            max = sum
        if sum < 0:
            sum =0

    return max

# 15. Roman to Integer
def roman_2_integer(roman):
    roman_map = { 'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000,
                  }
    result = 0
    for i in range(0, len(roman)):
        if i > 0 and roman_map[roman[i]] > roman_map[roman[i-1]]:
            result += roman_map[roman[i]] - 2 * roman_map[roman[i-1]]
        else:
            result += roman_map[roman[i]]
    return result

# 16 Single Number II
# Check later
def single_number_2(num_list, num):
    one = 0
    two = 0
    three = 0
    for i in num_list:
        two |= one & num_list[i];
        one ^= num_list[i];
        three = one & two;
        one &= ~three;
        two &= ~three;
    return one

# 17 Remove Element
def remove_element(num_list, elm):
    len = 0
    for i in range(len(num_list)):
        if num_list[i] != elm:
            num_list[len] = num_list[i]
            len+=1
    return len

# 18 Integer to Roman
# WOCAONIMA
def integer_2_roman(num):
    digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD' ),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ""
    while len(digits) > 0:
        (val, romn) = digits[0] # Unpacks the first pair in the list
        if n < val:
            digits.pop(0) # Removes first element
        else:
            n -= val
            result += romn
    return result

# 19 Merge two sorted list
# Wo dou bu xiang xiang le
def merge_sorted_list(list1, list2):
    head = None
    prev = None
    while list1 is not None and list2 is not None:
        if head is None:
            if list1.data < list2.data:
                head = Node(list1.data)
                list1 = list1.next
            else:
                head = Node(list2.data)
                list2 = list2.next
            prev = head
        else:
            if list2 is None or list1.data < list2.data:
                new = Node(list1.data)
                list1 = list1.next
            else:
                new = Node(list2.data)
                list2 = list2.next
            prev.next = new
            prev = new
    return head

# 20. Balanced Binary Tree
# need to check if there's a better way
def balanced_bt(root):
    if root is None:
        return True

    if abs(get_height(root.left) - get_height(root.right)) > 1:
        return False

    return balanced_bt(root.left) and balanced_bt(root.right)

def get_height(root):
    if root is None:
        return 0
    else:
        return max(get_height(root.left), get_height(root.right)) + 1

# 21. Convert sorted array to bst
def array_to_bst(num_list):
    if num_list is None:
        return None
    return array_to_bst(num_list, 0, len(num_list)-1)

def array_to_bst_helper(num_list, start, end):
    if start > end:
        return

    mid = (start + end) / 2
    n = treeNode(num_list[mid])
    n.left = array_to_bst_helper(num_list, start, mid - 1)
    n.right = array_to_bst_helper(num_list, mid + 1, end)

    return n

# 22. Remove Duplicates from sorted array
# Fuck remember it is length + 1 !!!!
def remove_duplicates_in_array(num_list):
    length = 0
    for i in range(1, len(num_list)):
        if num_list[i] != num_list[length]:
            length += 1
            num_list[length] = num_list[i]

    return length + 1

# 23. Pascal's Triangle
# Fuck notice it's range(n-1) not n
def pascal_triangle_2(n):
    if n == 1:
        return [1]
    prev = [1]
    result = [prev, ]
    for i in range(n-1):
        prev_copy = prev[:]
        prev_copy.append(0)
        prev_copy.insert(0,0)
        new_line = []
        # first and last num always assume 0
        for i in range(1, len(prev_copy)):
            new_line.append(prev_copy[i] + prev_copy[i-1])
        result.append(new_line)
        prev = new_line
    return result

# New way to think about this. Not appending 0 at beginning but append 1, and sum every other besides last one
# this is the fucking best way to do this
def pascal_triangle(n):
    if n == 1:
        return [1]
    prev = [1]
    result = [prev,]

    for i in range(n-1):
        new_line = []
        # appen first 1
        new_line.append(1)
        for j in range(1, len(prev)):
            new_line.append(prev[j] + prev[j-1])
        # append last 1
        new_line.append(1)
        result.append(new_line)
        prev = new_line

    return result

# 24. Merge sorted array
# code will be cleaner if pthon has --
def merge_sorted_array(l1, l2):
    end = len(l1) + len(l2) - 1         # this will be the new end
    end_1 = len(l1) - 1
    end_2 = len(l2) - 1
    while end_1 >= 0 and end_2 >= 0:
        if l1[end_1] >= l2[end_2]:
            l1[end] = l1[end_1]
            end_1 -= 1
        else:
            l1[end] = l2[end_2]
            end_2 -= 1
        end -= 1
    # if end_1 hit 0, then it's done. so only possibility is end_2 not hit zero
    while end_2 >= 0:
        l1[end] = l2[end_2]
        end -= 1
        end_2 -= 1

    return l1

# 25. Swap Nodes in Pairs
def swap_nodes(head):
    while head is not None and head.next is not None:
        temp = head.data
        head.data = head.next.data
        head.next.data = temp
        head = head.next.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    while head is not None:
        print head.data
        head = head.next


# 26. Symmetric Tree
def symmetric_tree(root):
    pass

# 27. Gray Code
def gray_code():
    pass

# 28. N-Queens II
def n_queens_ii():
    pass

# 29. Sort Colors
def sort_colors():
    pass

# 30. Binary Tree Level Order Traversal II
def bt_level_traversal_ii():
    pass

if __name__ == '__main__':
    #num_list = [1,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10]
    #print single_number(num_list)
    #print reverse_int(131)
    #print unique_bst(4)
    #num_list = [1,3,5,7,9,10]
    #target = 3
    #print search_insert_position_1(num_list, target)
    #print search_insert_position(num_list, target, 0, len(num_list)-1)
    #print roman_2_integer('MCMLIVx')
    #print pascal_triangle(5)
    """
    This is way fucking too easy. Why people want to use swap the real nodes?
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(10)
    print_list(head)
    swap_nodes(head)
    print 'shit'
    print_list(head)
    """
# Note for todo:
"""
1. check the best way to implement reverse_int. This is not a clever one
"""
