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
# This is a bit hard to think
def next_right_pointer(root):
    if root is None:
        return
    if root.left is not None:
        root.left.next = root.right
    if root.right is not None and root.next is not None:
        root.right.next = root.next.left
    next_right_pointer(root.left)
    next_right_pointer(root.right)

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

# Not using recursive, but also using extra space, so not a good result
def next_right_pointer(root):
    if root is None:
        return
    prev = [root,]
    while len(prev) > 0:
        current = []
        for i in range(1, len(prev)):
            prev[i-1].next = prev
            if node.left is not None:
                current.append(node.left)
            if node.right is not None:
                current.append(node.right)
        prev[-1].next = None
        prev = current[:]
    return root


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
    if root is None:
        return True

    return is_symetric(root.left, root.right)

def is_symmetric(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.data != q.data:
        return False
    else:
        return is_symmetric(p.left, q.right) and is_symmetric(p.right, q.left)

# 27. Gray Code
def gray_code(n):
    for x in range(n):
        print bin(n+x^x/2)[3:]
# A easy understandable way to solve this
def graycode(numbits, reverse = False):
    if numbits = 1:
        if reverse:
            yield "1"
            yield "0"
        else:
            yield "0"
            yield "1"
    else:
        if reverse:
            # all the "1"s start first
            gcprev = graycode(numbits - 1, True)
            for code in gcprev:
                yield "1" + code

            gcprev = graycode(numbits - 1, False)
            for code in gcprev:
                yield "0" + code
        else:
            # all the "0" start first
            gcprev = graycode(numbits - 1, False)
            for code in gcprev:
                yield "0" + code

            gcprev = graycode(numbits - 1, True)
            for code in gcprev:
                yield "1" + code

# 84. N-Queens
def n_queens(n):


def is_valid(result, r):
    for i in range(r):
        if result[i] == result[r] or abs((result[i]-result[r]) - (i-r)) == 0:
            return False
    return True


# 28. N-Queens II
def n_queens_ii():
    pass

# 29. Sort Colors
# Passing twice
def sort_colors(list):
    counter = [0] * 3
    for i in list:
        if i == 0:
            counter[0] += 1
        elif i == 1:
            counter[1] += 1
        else:
            counter[2] += 1
    result = [0] * counter[0] + [1] * counter[1] + [2] * counter[2]

    return result

# Not 100% sure about the result but looks all right
def sort_colors(list):
    index = 0
    red_index = 0
    blue_index = len(list) - 1

    while index <= blue_index:
        if list[index] == 0:             # red
            swap(list, index, red_index)
            index += 1
            red_index += 1
        elif list[index] == 2:           # blue
            swap(list, index, blue_index)
            index += 1
            blue_index -= 1
        else:
            index += 1

    return list


# 30. Binary Tree Level Order Traversal II
# Note: this returns a stack, in order to return a reverse one, still need to reverse them
def bt_level_traversal_ii(root):
    if root is None:
        return
    # Use pop() to pop the result later
    stack = [[root,],]
    prev = [root,]
    current = []
    while len(prev) > 0:
        for node in prev:
            if node.left is not None:
                current.append(node.left)
            if node.right is not None:
                current.append(node.right)
        if len(current) > 0:
            stack.append(current)
        prev = current
        current = []

    return stack

# 31. Permutations
# Need to fucking remember this. Divide and Conquer
def permute(num):
    if not num:
        return [[]]
    else:
        res = []
        for i, e in enumerate(num):
            rest = num[:i] + num[i + 1:]
            rest_perms = permute(rest)
            for perm in rest_perms:
                res.append( perm + [e,])
        return res

# 32. Generate Parentheses
def parentheses_gen(n):
        res = []
        cand = ''
        gp(n, n, cand, res)
        return res

def gp(left, right, cand, res):
    if left > right or left < 0:
        return
    elif left == 0 and right == 0:
        res.append(cand)
    else:
        gp(left - 1, right, cand + '(', res)
        gp(left, right - 1, cand + ')', res)

# 33. Best time to buy and sell II
# Fuck need to delete the previous work
def stock_buy_sell_I(prices):
    min_price = prices[0]
    max_profit = prices[0]
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_pirce = min(min_price, price)
    return max_profit

def stock_buy_sell_II(prices):
    profit = 0
    prev = price[0]
    for price in prices[1:]:
        if price >= prev:               # Increasing
            profit += price - prev
        prev = price
    return profit
"""
Wrong solution
def stock_buy_sell_III(prices):
    profit_2 = [0] * 2
    prev = price[0]
    low_price = price[0]

    for price in prices[1:]:
        if price < prev:                 # Reached high point/decreasing, calculate profit, got new low_price
            profit = low_price - prev
            if prev != low_price:        # Means this is the high point
                profit_2 = calculate_max_2(profit, profit_2)
            low_price = price
        prev = price
    # Need to calcualte the last one
    profit_2 = calculate_max_2(prev - low_price, profit_2)
    return profit_2
"""
# A little bit Dynamic Programming
# 1. in-order pass: use profit = price - min_price
# 2. back-order pass: use profit = max_price - price

def stock_buy_sell_III(prices):
    n = len(prices)
    m1 = [0] * n
    m2 = [0] * n
    max_profit1 = 0
    min_price1 = prices[0]
    max_profit2 = 0
    max_price2 = prices[-1]
    # It's O(3n) which is O(n)
    for i in range(n):
        max_profit1 = max(max_profit1, prices[i] - min_price1)
        m1[i] = max_profit1
        min_price1 = min(min_price1, prices[i])
    for i in range(n):
        max_profit2 = max(max_profit2, max_price2 - prices[n - 1 - i])
        m2[n - 1 - i] = max_profit2
        max_price2 = max(max_price2, prices[n - 1 - i])
    max_profit = 0
    for i in range(n):
        max_profit = max(m1[i] + m2[i], max_profit)
    return max_profit

# 34. Plus One
# Fuck you cheat guys
def plus_one(digits):
  pass

# 35. Roatate Image
def rotate_image(matrix):
    rotated = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)-1, -1, -1): # from n-1 to 0
            new_row.append(matrix[i][j])
        rotated.append(new_row)
    return rotated

# Fuck remember this is different from the 150Ti
def link_list_cycle(head):
    slow_runner = head
    fast_runner = head
    while fast_runner is not None and fast_runner.next is not None:
        fast_runner = fast_runner.next
        slow_runner = slow_runner.next
        if fast_runner == slow_runner:
            return True
    return False

# 36. Linked List Cycle II
def link_list_cycle_II():
    slow_runner = head
    fast_runner = head
    while fast_runner != slow_runner:
        if fast_runner is None or fast_runner.next is None:
            return None
        else:
            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next
    # Met each other, so that's a loop
    fast_runner = head
    while fast_runner != slow_runner:
        fast_runner = fast_runner.next
        slow_runner = slow_runner.nexdt

    return slow_runner

# 37. Unique Path
def unique_path(m,n):
    if (m, n) == (0,0):
        return 0
    elif (m, n) in [(1,0), (0,1)]:
        return 1
    elif m == 0:
        return unique_path(m, n-1)
    elif n == 0:
        return unique_path(m-1,n)
    else:
        return unique_path(m-1,n) + unique_path(m, n-1)

def unique_path_ii(map, m, n):
    if (m, n) == (0,0):
        return 0
    elif (m,n) in [(1,0),(0,1)]:
        return 1
    else:
        if not valid_point(map, m-1, n) and not valid_point(map, m, n-1): # No where to go
            return 0
        elif valid_point(map, m-1, n) and valid_point(map, m, n-1):       # Can go both directions
            return unique_path_ii(map, m-1, n) + unique_path_ii(map, m, n-1)
        else:                                                             # Can only go one direction
            if valid_point(map, m-1, n):
                return uniqe_path_ii(map, m-1, n)
            else:
                return unique_path_ii(map, m, n-1)

def valid_point(map, m, n):
    if m < 0 or n < 0:
        return False
    if map[m][n] == 1:
        return False
    return True
# This solution may look a bit stupid


# 38. Binary Tree Postorder Traversal
# Doing recursive is trivial
def bt_post_traversal(root):
    if root is None:
        return
    bt_post_traversal(root.left)
    bt_post_traversal(root.right)
    print root.data

# Any pre/in/post-order tree traversal are all dfs which use stack
def bt_post_traversal(root):
    if root is None:
        return
    stack1 = [root,]
    stack2 = []
    while len(stack1) > 0:
        node = stack1.pop()
        stack2.append(node.data)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
    path = []
    while stack2:
        path.append(stack2.pop())
# Need to go back and check the logic to do so


# 39. Binary Tree Level Order Traversal
def bt_level_order_traversal(root):
    if root is None:
        return []
    result = [[root]]
    current = []
    prev = [root,]
    while len(prev):
        for node in prev:
            if node.left is not None:
                current.append(node.left)
            if node.right is not None:
                current.append(node.right)
        if len(current) > 0:
            result.append(current)
        prev = current
        current = []

    return result

# 40. Container With Most Water
# Thinking this (i, ai) and (i, 0)
# so for pair (m, n)
# area is abs(m-n) * min(am, an)
def most_water(plist):
    max_volumn = 0
    for i, pm in enumerate(plist):
        for pn in plist[i+1:]:
            max(max_volumn, calculate_area(pm, pn))

    return max_volumn

def calculate_area(pm, pn):
    return abs(pm[0] - pn[0]) * min(pm[1], pn[1])

# My algorithm is correct, this use greedy algorithm
def maxArea(height):
    n = len(height)
    i = 0
    j = n - 1
    max_area = 0
    while i < j:
        max_area = max(max_area, (j - i) * min(height[i], height[j]))
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
return max_area

# 41. Minimum Path Sum
# Strong feel that I did correctly, but need to check more. The result on website is almost same with mine
# Online result is doing a map, each point is the sum till current position.
def min_path_sum(grid):
    return min_path_helper(grid, m, n, 0)

def min_path_helper(grid, m, n, sum):
    if (m, n) == (0, 0):
        return sum
    elif m == 0 or n == 0:              # Reach the bound
        if m == 0:
            return min_path_helper(m, n-1, sum+grid[m][n])
        else:
            return min_path_helper(m-1, n, sum+grid[m][n])
    else:                               # Normal one
        return min(min_path_helper(m, n-1, sum+grid[m][n]), min_path_helper(m, n-1, sum+grid[m][n]))
# Above is the recursive way. I think iterative way should be better
def min_path_sum(grid):
    m = len(grid[0])
    n = len(grid)
    t = [ [0] * m ] * n
    for j in range(m):                  # Go up/left doesnt' matter, important is result
        for i in range(n):
            if i == 0 and j ==0:
                t[i][j] = grid[i][j]
            elif i == 0:
                t[i][j] = t[i][j-1] + grid[i][j]
            elif j == 0:
                t[i][j] = t[i-1][j] + grid[i][j]
            else:
                t[i][j] = min(t[i-1][j], t[i][j-1]) + grid[i][j]

    return t[m-1][n-1]


# 42. Search a 2D Matrix
# !! Remember that binary search is start <= end !!!!
def search_2d_matrix(matrix, target):
    m = len(matrix[0])
    n = len(matrix)

    start = 0
    end = n - 1
    while start < end:
        row_mid = (start+end)/2
        if matrix[row_mid][0] <= target and matirx[row_mid][-1] >= target: # search for this row
            start = 0
            end = m-1
            while start <= end:
                col_mid = (start+end)/2
                if matrix[row_mid][col_mid] == target:
                    return True
                elif matrix[row_mid][col_mid] > target: # need to search front half
                    end = mid -1
                else:
                    start = mid + 1
            return False
        elif matrix[row_mid][0] > target: # search for front half
            end = row_mid - 1
        else:
            start = row_id + 1
    return False

# 43. Set Matrix Zeroes
# There's a better way which can save the space of doing so'
def set_matirx_0(matrix):
    m = len(matrix[0])
    n = len(matrix)
    zero_row = False
    zero_col = False

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0:
                    zero_row = True
                if j == 0:
                    zero_col = True
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if zero_row:
        for j in range(m):
            matrix[0][j] = 0
    if zero_colum:
        for i in range(n):
            matrix[i][0] = 0

    return matrix

# 44. Path Sum
# in a pretty good shape
def has_path_sum(root, target):
    if root is None:
        return False

    elif root.left is None and root.right is None: # Found a leaf
        if target == root.data:
            return True
        else:
            return False
    else:
        target -= root.data
        return has_path_sum(root.left, target) or has_path_sum(root.right, target)

# 45. Remove Duplicates from Sorted Array II
# Note: we have 4 types of questions: Remove dup from sorted array i/ii and list i/ii
def remove_dup_array_II(array):
    current = 0
    counter = 0
    n = len(array)
    for i in range(1, n):
        if array[i] == array[i-1]:      # Found a dup
            counter += 1
        else:
            if counter > 0:
                pass
            else:
                array[current] = array[i-1]
                current += 1
            counter = 0
    if counter == 0:
        array[current] = array[n-1]
        current += 1
    if current > 1:
        return array[:current]
    else:
        return []


# 46. Spiral Matirx II
def spiral_matrix_II(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    start_row = start_col = 0
    end_row = end_col = n -1
    num = 1
    while start_row < end_row and start_col < end_col:
        for i in range(start_col, end_col+1): # Go right
            matrix[start_row][i] = num
            num += 1
        for i in range(start_row+1, end_row+1): # Go down
            matrix[i][end_col] = num
            num += 1
        for i in range(end_col-1, start_col-1, -1): # Go left
            matrix[end_row][i] = num
            num += 1
        for i in range(end_row-1, start_row, -1): # Go up
            matrix[i][start_col] = num
            num += 1
        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1
    if n % 2 == 1:
        matrix[start_row][start_colum] = num
    return matrix

# 47. Pascal's Triangle II
def pascal_triangle_II(n):
    from collections import deque
    result = deque()
    for i in range(n-1):
        for j in range(0, len(result)-1):
            result[j] = result[j] + result[j+1]
        result.appendleft(1)
    return result

# 48. Combinations
# Remember in this question, result need to use result[:] as copy
def combine(n, k):
    ret = []
    def combine_helper(result):
        if len(result) == k:
            ret.append(result[:])
            return
        elif len(result) == 0:
            start = 1
        else:
            start = result[-1] + 1
        if start > n:
            return
        else:
            for i in range(start, n+1):
                result.append(i)
                combine_helper(result)
                result.pop()
    combine_helper([])
    print ret

# 49. Search in Rotated Sorted Array II/I
# Don't be afraid of this problem. It's very simple once you know what to do
def search_rot_array_i(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) / 2
        if target == array[mid]:
            return True
        if array[mid] > array[start]: # First half sorted
            if array[start] <= target and target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:                           # Second half sorted
            if array[mid] < target and target <= array[end]:
                start = mid + 1
            else:
                end = mid -1

    return False

# Introducing the situation that dupliate element, but actually they are same
# When there are dup element, just keep on moving
def search_rot_arrary_II():
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) / 2
        if target == array[mid]:
            return True
        if array[mid] > array[start]:                  # First half sorted
            if array[start] <= target and target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif array[mid] < array[start]:                # Second half sorted
            if array[mid] < target and target <= array[end]:
                start = mid + 1
            else:
                end = mid -1
        else:                                          # array[mid] == array[start]
            start += 1
    return False

# 50. Remove Nth Node From End of List
# Too lazy to check if it is correct
def remove_nth_end(head, n):
    if head is None:
        return
    slow = head
    fast = head
    for i in range(n):
        if fast.next is None:
            return
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow.data

# 51. Populate Next Right Pointers in Each Node II
# A bit hard to think, need to slow down
def pop_next_pointers_ii(root):
    if root is None:
        return
    head = None
    prev = None
    while root is not None:
        while root is not None:
            if root.left is not None:
                if prev is None:
                    prev = head = root.left
                else:
                    prev.next = root.left
                    prev = prev.next

            if root.right is not None:
                if prev is None:
                    prev = head = root.right
                else:
                    prev.next = root.right
                    prev = prev.next
            root = root.next

        root = head
        prev = None
        head = None
    return


# 52. Palindrome Number
def palindrome(num):
    if num < 0:
        return False

    div = 10
    while num/div > 0:
        div *=10

    while num > 0:
        left_bit = num/div
        right_bit = num % 10

        if left_bit != right_bit:
            return False
        else:
            num = (num % div) / 10
            div /= 100
    return True

# 53. Minimum Depth of Binary Tree
def min_depth_of_bt(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    elif root.left is None:
        return min_depth_of_bt(root.right) + 1
    elif root.right is None:
        return min_depth_of_bt(root.left) + 1
    else:
        return min(min_depth_of_bt(root.left), min_depth_of_bt(root.right)) + 1

# 54. Sum Root to Leaf Numbers
def sum_root_to_leaf(root):
    if root is None:
        return 0
    result = 0

    def sum_root_to_leaf_helper(node,value):
        value = value * 10 + node.data
        if node.left is None and node.right is None:
            result += value
            return
        if node.left is not None:
            sum_root_to_leaf_helper(node.right, value)

        if node.right is None:
            sum_root_to_leaf_helper(node.left, value)

    sum_root_to_leaf_helper(root,root.data)


# 55. Length of Last Word
# This a python way, even not the python way, it's too easy
def len_last_word(str):
    word_list = str.split(' ')
    return len(word_list[-1])

def len_lst_word(str):
    if str[-1] == ' ':
        return 0
    for i, char in enumerate(str[::-1]):
        if char == ' ':
            return i

# 56. Trapping Rain Water
# Haven't finished yet
def trap_rain_water(data_list):
    pass

# 57. Search in Rotated Sorted Array
# See 49.

# 58. Valid Parenetheses
def valid_paren(parens):
    pair = dict( '[' : ']', '{' : '}', '(' : ')' )
    if parens[0] in [']','}',')']:
        return False
    stack = []
    stack.append(parens[0])
    for i in range(1, len(parens)):
        if parens[i] in ['[','{','(']:
            stack.append(parens[i])
        else:
            if not stack:
                return False
            current = stack[-1]
            if pair.get(current) != parens[i]:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True


# 59. Valid Sudoku
def valid_sudoku(board):
    if len(board) != 9 or len(board[0]) !=9:
        return False
    for i in range(9):
        row = []
        column = []
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in row:
                    return False
                else:
                    row.append(board[i][j])
            if board[j][i] != '.':
                if board[j][i] in column:
                    return False
                else:
                    column.append(board[j][i])

    for i in range(0,9,3):
        for j in range(0,9,3):
            for x in range(i, +3):
                for y in range(j, j+3):
                    if board[x][y] == '.':
                        continue
                    if board[x][y] in num:
                        return False
                    else:
                        num.append(board[x][y])
    return True


# 60. Path Sum II
# Should be correct
def path_sum_ii(root, target):
    if root is None:
        return []
    paths = []
    def path_sum_helper(node, result, target):
        result.append(node.value)
        if node.left is None and node.right is None and target == node.data:
            paths.append[result[:]]
            return
        elif target <= node.data:                # Stop this path
            result.pop()
            return
        else:                           # target > 0, child exist
            if node.left is not None:
                path_sum_helper(node.left, result, target-node.data)
            if node.right is not None:
                path_sum_helper(node.right, result, target-node.data)
        result.pop()
    path_sum_helper(root, [], target)

# 61. Subsets
# SOOOOOOO Niu Bi
def sub_sets(list):
    ret = [[]]
    def sub_sets_helper(result, list):
        for i, item in enumerate(list):
            result.append(item)
            ret.append(result[:])
            sub_sets_helper(result, list[i+1:])
            result.pop()
    sub_sets_helper([], list)
    return ret

# 62. Unique Path
# check 37
def unique_path_ii():
    pass

# 63. Jump Game
# So many boundary problem
def jump_game(jump_list):
    length = len(jump_list)
    for i, height in enumerate(jump_list[::-1]):
        if height == 0:
            require = 1
            location = length - i - 1
            while location >= 0:
                if require < jump_list[location]:
                    break
                else:
                    require += 1
                    location -= 1
            if location < 0:
                return False
    return True

# 64. Flatten Binary Tree to Linked List
# This is different from the web, need to check if this is also correct
def flat_bt(root):
    if root is None:
        return None

    if head is None:
        head = root
    else:
        head.next = root
        head = head.next

    flat_bt(root.left)
    flat_bt(root.right)
    root.left is None
    root.right is None

# 65. Longest Consecutive Sequence
def longest_con_seq():
    pass

# 66. Subsets II
def sub_setes_ii():
    pass

# 67. Longest Common Prefix
def longest_com_pre():
    pass

# 68. Search for a Range
def search_for_range():
    pass

# 69. 3 Sum Closest
def three_sum_closest():
    pass

# 70. Convert Sorted List to Binary Search Tree
# A bit tricky when need to check head == slow
def convert_to_bst(head):
    if head is None:
        return None
    slow = head
    fast = head
    prev = None
    while fast.next is not None and fast.next.next is not None:
        prev = slow
        fast = fast.next.next
        slow = slow.next                # slow is what we are looking for
    if head == slow:
        head = None
    # Create two separate linklists
    if prev is not None:
        prev.next = None
    node = Node(slow.data)
    node.left = convert_to_bst(head)
    node.right = convert_to_bst(slow.next)
    return node

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
