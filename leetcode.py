#!/usr/bin/env python

# 1.Single Number
# Fuck!!! use XOR
def single_number(num_list):
    for num in num_list[1:]
        if num is not None:
            num_list[0] ^= num
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
    if p is None or q is None:
        return False
    if p.data != q.data:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# 4.Reverse Integer
def reverse(x):
    if x < 0:
        return (-1) * reverse( (-1) * x)
    res = 0
    while x > 0:
        res = res*10 + x%10
        x /= 10
    return res

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
# Iterative way
def inorder_traversal(root):
    stack = []
    res = []
    current = root
    while current is not None or len(stack)>0:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack)>0:
            current = stack.pop()
            res.append(current.val)
            current = current.right
    return res

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print root.data
    inorder_traversal(root.right)

# 9. BT Preorder traversal
# Iterative way
def preorder_traversal(root):
    stack = []
    current = root
    while current is not None or len(stack)>0:
        if current is not None:
            res.append(current.val)
            stack.append(current)
            current = current.left
        elif len(stack)>0:
            current = stack.pop()
            current = current.right
    return res

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

"""
Need to validate if this is correct
def next_right_pointer(root):
    if root is None:
        return

    left = root.left
    right = root.right

    if left is not None and right is not None:
        left.next = right

    while left.right is not None:
        left = left.right
        right = right.left
        left.next = right

    next_right_pointer(root.left)
    next_right_pointer(root.right)
"""

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
def searchInsert(A, target):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:       # need to search second half
            start = mid + 1
        else:
            end = mid - 1
    return start

# Too easy way, not the way wanted
def searchInsert_2(A, target):
    for i, num in enumerate(A):
        if target <= num:
            return i
        return len(A)

"""
Guess these two are not the best ways
def search_insert_position_1(num_list, num):
    i = 0
    while i <= len(num_list)-1:
        if num <= num_list[i]:
            return i
        i += 1
    return i

# No need to use recursive
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
"""

# 12. Remove Duplicates from Sorted List:
def deleteDuplicates(self, head):
    if head is None or head.next is None:
        return head
    current = head
    while current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

"""
No need to use prev
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
"""
# 13. Climbing Stairs
# Fuck you remember the num <= 2
# There's a way not to use recursive
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
# dp way
# dp[i] = max(A[i], dp[i-1]+A[i])
# Note        here    it's A[i] not dp
# Because we don't need to store dp[i], so simplify to dp
def maxSubArray_2(self, A):
    res = A[0]
    dp = A[0]
    for num in A[1:]:
        dp = max(num, dp+num)
            res = max(res, dp)
    return res

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
def remove_element(A, elem):
    i = 0
    for j, num in enumerate(A):
        if num != elem:
            A[i] = A[j]
            i += 1
    return i

# 18 Integer to Roman
# WOCAONIMA
def integer_2_roman(num):
    digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD' ),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ""
    for digit in digits:
        while num >= digit[0]:
            result += digit[1]
            num -= digit[0]
        if num == 0:
            break
    return result

"""
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
"""
# 19 Merge two sorted list
# Wo dou bu xiang xiang le
# Using dummy make life easier
def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 is not None:
        cur.next = l1
    if l2 is not None:
        cur.next = l2
    return dummy.next
"""
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
"""

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
# Remember i+1, also don't forget lenght check
def removeDuplicates_2(A):
    if len(A) <= 1:
        return len(A)
    i = 0
    for j in range(1, len(A)):
        if A[i] != A[j]:
            A[i+1] = A[j]
            i += 1
    return i+1
"""
# Fuck remember it is length + 1 !!!!
def remove_duplicates_in_array(num_list):
    length = 0
    for i in range(1, len(num_list)):
        if num_list[i] != num_list[length]:
            length += 1
            num_list[length] = num_list[i]

    return length + 1
"""
# 23. Pascal's Triangle
# Fuck notice it's range(n-1) not n
def generate_1(numRows):
    res = []
    for j in range(numRows):
        current = [1]
        for i in range(1, j):
            current.append(res[-1][i]+res[-1][i-1])
        if j>=1:
            current.append(1)
        res.append(current[:])
    return res
"""
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
"""
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
    elif p is None or q is None or p.data != q.data:
        return False
    else:
        return is_symmetric(p.left, q.right) and is_symmetric(p.right, q.left)

# Iterative way
def isSymmetric_2(root):
    if root is None:
        return True
    queue = collections.deque()
    queue.append(root.left)
    queue.append(root.right)
    while len(queue)>0:
        t1 = queue.popleft()
        t2 = queue.popleft()
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None or t1.val != t2.val:
            return False
        queue.append(t1.left)
        queue.append(t2.right)
        queue.append(t1.right)
        queue.append(t2.left)
    return True

# 27. Gray Code
def grayCode(n):
    i = 0
    ret = []
    while i < 2**n:
        ret.append(i>>1^i)
        i += 1
    return i

# This is better than below one which is easier to remember,
# But this question, we want int instead of string binary
def grayCodeGen(n):
    if n == 1:
        return ['0', '1']
    else:
        ret = []
        code_list = grayCodeGen_2(n-1)
        for code in code_list:
            ret.append('0' + code)
        for code in code_list[::-1]:
            ret.append('1' + code)
        return ret

# A easy understandable way to solve this
def graycode(numbits, reverse = False):
    if numbits == 1:
        if reverse:
            yield "1"
            yield "0"
        else:
            yield "0"
            yield "1"
    else:
        if reverse:
            # all the "1"s start first
            gcprev = graycode(numbits - 1, False)
            for code in gcprev:
                yield "1" + code
            gcprev = graycode(numbits - 1, True)
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
    pass

def is_valid(result, r):
    for i in range(r):
        if result[i] == result[r] or abs((result[i]-result[r]) - (i-r)) == 0:
            return False
    return True


# 28. N-Queens II
def n_queens_ii():
    pass

# 29. Sort Colors
# Passing only once
def sort_colors(A):
    index = 0
    red_index = 0
    blue_index = len(A) - 1
    while index <= blue_index:
        if A[index] == 0:             # red
            swap(A, index, red_index)
            index += 1
            red_index += 1
        elif A[index] == 2:           # blue
            swap(A, index, blue_index)
            index += 1 # Remember this index won't increase
            blue_index -= 1
        else:
            index += 1
    return A

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
# With simpler implementation
def generateParenthesis(n):
    ret = []
    generateParenthesis_helper(n, n, '', ret)
    return ret

def generateParenthesis_helper(left, right, res, ret):
    if left == 0 and right ==0:
        ret.append(res[:])
        return
    if left > 0:
        generateParenthesis_helper(left-1, right, res+'(', ret)
    if right > left:
        generateParenthesis_helper(left, right-1, res+')', ret)

"""
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
"""
# 33. Best time to buy and sell II
# Remember to pre check

def stock_buy_sell_I(prices):
    if len(prices) < 1:
        return 0
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
# Remember to set slow = head.next and fast = head.next.next before entering the loop
def link_list_cycle_II():
    if head is None or head.next is None:
        return None
    slow = head.next
    fast = head.next.next
    while slow!=fast:
        if fast is None or fast.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
    fast = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow

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
# Doing in iterative way

def bt_post_traversal(root):
    stack = [root]
    output = []
    while len(stack)>0:
        node = stack.pop()
        output.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return output[::-1]

# Doing recursive is trivial
def bt_post_traversal(root):
    if root is None:
        return
    bt_post_traversal(root.left)
    bt_post_traversal(root.right)
    print root.data

# Any pre/in/post-order tree traversal are all dfs which use stack

# 39. Binary Tree Level Order Traversal
def levelOrder(root):
    res = []
    if root is None:
        return res
    queue = []
    level = []
    queue.append(root)
    queue.append(None)
    while len(queue)>0:
        node = queue.pop(0)
        if node is None:
            res.append(level[:])
            level = []
            if len(queue)>0:
                queue.append(None)
        else:
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return res

"""
The problem here is we want a result in int, but not copy the node
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
"""
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
# Simpler way
def combine(n, k):
    ret =[]
    combine_helper(1, n, k, [], ret)
    return ret
def combine_helper(cur, n, k, res, ret):
    if len(res) == k:
        ret.append(res[:])
        return
    for i in range(cur, n+1):
        res.append(i)
        combine_helper(i+1, n, k, res, ret)
        res.pop()
"""
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
"""
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
# Simpler code
def isValid(s):
    bracket_dict = { '[' : ']',
                     '{' : '}',
                     '(' : ')',
                     }
    stack = []
    for bracket in s:
        if bracket in bracket_dict.keys():
            stack.append(bracket)
        elif len(stack) == 0 or bracket !=bracket_dict[stack.pop()]:
            return False
        return len(stack) == 0
"""
# Remember, here cannot use dict() to define '[' as a key
def valid_paren(parens):
    pair = { '[' : ']',
             '{' : '}',
             '(' : ')'}
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
"""

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
def subsets(S):
    ret = []
    subsets_helper(0, sorted(S), [], ret)
    return ret

def subsets_helper(i, S, res, ret):
    if i == len(S):
        ret.append(res[:])
        return
    subsets_helper(i+1, S, res, ret) # No element i
    res.append(S[i])
    subsets_helper(i+1, S, res, ret) # With element i
    res.pop()

"""
New answer has better understanding
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
"""
# 62. Unique Path
# check 37
def unique_path_ii():
    pass

# 63. Jump Game
# Better way to do this, think as a dp
def jump_game(jump_list):
    N = len(jump_list)
    start = 0
    max_cover = 0
    while start <= max_cover and max_cover < N-1:
        max_cover = max(start+jump_list[start], max_cover)
        start += 1
    return max_cover >= N-1

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
def longest_con_seq(list):
    from sets import Set
    d = Set
    longest = 1
    for i in list:
        if i not in d:
            d.add(i)
    for item in d:
        cur = item
        cur_len = 1
        while cur+1 in d:
            cur_len += 1
            cur +=1
        longest = max(longest, cur_len)
    return longest

# 66. Subsets II
# There's another version of doing subsets. But almost the same.
def sub_sets_ii(list):
    ret = [[]]
    def sub_sets_helper(result, list):
        for i, item in enumerate(list):
            result.append(item)
            if result[:] not in ret:
                ret.append(result[:])
            sub_sets_helper(result, list[i+1:])
            result.pop()
    sub_sets_helper([], list)
    return ret

# 67. Longest Common Prefix
# Tricky is no need to set flag or anything. Just return the result
def longest_common_prefix(list_str):
    if len(list_str) == 0:
        return None
    elif len(list_str) == 1:
        return list_str[0]
    compare = list_str[0]
    length = len(compare)
    i = 0
    while i < length:
        for stri in list_str[1:]:
            if i > len(stri)-1 or stri[i] != compare[i]:
                return compare[:i]
        i += 1
    return compare

# Use a quick way but not the Big-O best one
def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    print s1, s2
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

# 68. Search for a Range
# Perfect for one time
def search_for_range(target, list):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) / 2
        if list[mid] == target:
            start = end = mid
            while True:
                if list[start] != target and list[end] != target:
                    return (start+1, end-1)
                if list[start] == target:
                    start -= 1
                if list[end] == target:
                    end += 1
        elif list[mid] < target:        # need to search second half
            start = mid + 1
        else:
            end = mid - 1
    return (-1,-1)

# 69. 3 Sum Closest
# This time cannot remember it. This is a weird solution. Need to think hard next time.
def three_sum_closest(list, target):
    list.sort()
    n = len(list)
    res = list[0] + list[1] + list[2]
    for i in range(n-2):
        start = i + 1
        end = n - 1
        sum = list[i] + list[start] + list[end]
        if abs(sum-target) < abs(res-target):
            res = sum
        if sum == target:
            return sum
        elif sum < target:
            start += 1
        else:
            end -= 1
    return res


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


# 71. Count and Say
# Will use the num as itself here. So easy
def count_n_say(string):
    result = ''
    prev = string[0]
    count = 1
    for char in string[1:]:
        if char == prev:
            count += 1
        else:
            result += str(count) + ' ' + prev
            if count > 1:
                result += 's '
            else:
                result += ' '
            prev = char
            count = 1
    result += str(count) + ' ' + prev
    if count > 1:
        result += 's'
    return result

# 72. Triangle
# way to thinking is too diao
def triangle(triangle):
    if triangle is None:
        return 0
    for i in range(len(triangle) - 2, -1, -1):
        for j, value in enumerate(triangle[i]):
            triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

# 73. Unique Binary Search
# Remember it's multiply but not plus
# Wrong one, this is unique bst i, but not ii
def unique_bs(list):
    if len(list) <= 2:
        return len(list)
    result = 0
    for i, num in enumerate(list):
        result += unique_bs(list[:i]) * unique_bs(list[i+1:])
    return result

# Need to write this again
def unique_bs_ii(n):
    a = range(1, n + 1)
    return unique_bs_ii_helper(a)

def unique_bs_ii_helper(a):
    if not a:
        return [None]
    else:
        res = []
        for i, c in enumerate(a):
            left = unique_bs_ii_helper(a[:i])
            right = unique_bs_ii_helper(a[i + 1:])
            for l in left:
                for r in right:
                    root = TreeNode(c)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

# 74. Binary Tree Zigzag Level Order Traversal
def zizag_traversal(root):
    result = [[root]]
    prev = deque(root)
    normal_order = False
    current = deque()
    while len(prev) > 0
        while len(prev) > 0:
            node = prev.pop()
            if normal_order:
                if node.left is not None:
                    current.append(node.left)
                if node.right is not None:
                    current.append(node.right)
            else:
                if node.right is not None:
                    current.append(node.right)
                if node.left is not None:
                    current.append(node.left)
        if len(current) > 0:
            result.append(current)
        prev = current
        normal_order = not normal_order
    return result

# 75. Partition List
def partition_list(head, target):
    if head is None:
        return None
    while head is not None:
        if head.data <= target:
            if left_start is None:
                left_start = head
                left_end = left_start
            else:
                left_end.next = head
                left_end = left_end.next
        else:
            if right_start is None:
                right_start = head
                right_end = head
            else:
                right_end.next = head
                right_end = right_end.next
        head = head.next
    if left_start is None:
        return right_start
    else:
        left_end.next = right_start
        return left_start

# 76. Combination Sum
# Don't forget to use copy[:]
def combinationSum(candidates, target):
    ret = []
    combinationSum_helper(sorted(candidates), target, [], ret) # Look into the question, need sorted
    return ret

def combinationSum_helper(candidates, target, res, ret):
    if target < 0:
        return
    elif target == 0:
        ret.append(res[:])
        return
    for i, num in enumerate(candidates):
        res.append(num)
        combinationSum_helper(candidates[i:], target - num, res, ret)
        res.pop()
"""
def comb_sum(list, target):
    ret = []

    def comb_sum_helper(list, target, result):
        if target < 0:
            return
        elif target == 0:
            ret.append(result[:])
            return
        for i in list:
            result.append(i)
            comb_sum_helper(list[i:], target-i, result)
            result.pop()

    comb_sum_helper(list, target, [])
    return ret
"""
# Combination Sum II
# No duplicate item should be used, what I see diff is list[i:] or list[i+1:], needs to be tested
# Bei Ni Ya Cai Dui le

# 77. Pow(x,n)
# WTF is this???
def pow_func(x,n):
    if n ==0:
        return 1
    elif n < 0:
        return 1 / pow_func(x, -n)
    else:
        v = pow_func(x, n/2)
        if n % 2 ==0:
            return v*v
        else:
            return v*v*x


# 78. Construct Binary Tree from Inorder and Postorder Traversal
def contruct_bt_ip(preorder, inorder):
    if len(inorder) == 0:
        return None

    root = treeNode(preorder.pop(0))
    root_index = inorder.index(root.data)
    root.left = construct_bt_ip(preorder, inorder[:root_index])
    root.right = construct_bt_ip(preorder, inorder[root_index+1:])
    return root

# 79.Letter Combination of a Phone Number
# Easy piece
def phone_num(digits):
    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',}
    ret = []
    def phone_num_helper(i, digits, result):
        if i == len(digits):
            ret.append(result[:])
            return
        for char in digit_map[digits[i]]:
            result.append(char)
            phone_num_helper(i+1, digits, result)
            result.pop()
    phone_num_helper(0,digits,[])
    return ret

# 80. FUCK this is empty

# 81. Construct Binary Tree from Preorder and Inorder Traversal
# Should be correct. This is almost the same to 78
def contruct_bt_pi(postorder, inorder):
    if len(inorder) == 0:
        return None
    root = treeNode(postorder.pop())
    root_index = inorder.index(root.data)
    root.left = construct_bt_pi(postorder, inorder[:root_index])
    root.right = construct_bt_pi(postorder, inorder[root_index+1:])
    return root

# 82. Palindrome Partitioning
# Not 100% sure it's correct, but will discuss it later
def palin_parti(string):
    ret = []

    def palin_parti_helper(s, result):
        if not s:
            ret.append(result[:])
        else:
            for i in range(len(s)):
                if is_palindrome(s[:i+1]):
                    result.append(s[:i+1])
                    palin_parti_helper(s[i+1:], result)
                    result.pop()
    def is_palindrome(s):
        start = 0
        end = len(s) -1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

# 83. Reverse Linked List II
# Really don't want to think about it right now
def reverse_list_ii(head, m, n):
    i = 1
    while head is not None and i <= n:
        if i < m-1:
            head = head.next
            i += 1
        elif i == m-1:
            start_tail = head
            reverse_end = head.next
            prev = None
            head = head.next
            i += 1
        elif i >=m and i <n:
            next = head.next
            head.next = prev
            prev = head
            head = next
            i += 1
        elif i == n:
            start_tail.next = reverse_head
            reverse_end.next = head.next

# 84. N-Queens
# There's also n queens ii
# I think this is correct, but need deep validation
# valid check isn't efficient
# This is not correct, n queens question is n*n chessboard but not always 8*8
def solveNQueens(n):
    ret = []
    res = ['.'*n for i in range(n)]
    solveNQueens_helper(n, res, ret, 0)
    return ret

def solveNQueens_helper(n, res, ret, queens):
    if queens == n:
        ret.append(res[:])
        return
    for i in range(n):
        new_row = '.'*n
        res[queens] = new_row[:i] + 'Q' + new_row[i+1:]
        if is_valid(res, queens, i):
            solveNQueens_helper(n, res, ret, queens+1)
        res[queens] = new_row

def is_valid(board, row, col):
    for i in range(row):
        for j in range(len(board[0])):
            if board[i][j] == 'Q' and (j == col or abs(row-i) == abs(col-j)):
                return False
    return True
"""
def n_queens(n):
    result = ['.' for i in range(8)]
    ret = []

    def n_queens_helper(i, result, queens):
        if queens == 0:
            ret.append(result[:])
        for j in range(8):
            result[i] = j
            if is_valid_result(result, i):
                n_queens_helper(i+1, result, queens-1)
            result[i] = '.'

    def is_valid_result(result, i):
        for j in range(i):
            if result[i] == result[j] or abs(result[i]-result[j]) == abs(i-j):
                return False
        return True

    n_queens_helper(0, result, n)
    return ret

def n_queens_ii(n):
    result = ['.' for i in range(8)]
    ret = 0

    def n_queens_helper(i, result, queens):
        if queens == 0:
            ret += 1
        for j in range(8):
            result[i] = j
            if is_valid_result(result, i):
                n_queens_helper(i+1, result, queens-1)
            result[i] = '.'

    def is_valid_result(result, i):
        for j in range(i):
            if result[i] == result[j] or abs(result[i]-result[j]) == abs(i-j):
                return False
        return True

    n_queens_helper(0, result, n)
    return ret
# Don't know what's the diff, just return a num += 1
"""
# 85. Validate Binary Search Tree
# Best way to do this in recursion
def valid_bst(root):
    return valid_bst_helper(root, INT_MIN, INT_MAX)

def valid_bst_helper(node, min, max):
    if node is None:
        return True
    if node.data <= min or node.data >= max:
        return False
    return valid_bst_helper(node.left, min, node.data) and valid_bst_helper(node.right, node.data, max)


# 86. Add Binary
# Pad with zeros
def add_binary(a, b):
    int_a = [ int(i) for i in a]
    int_b = [ int(i) for i in b]
    carry = 0
    result = []
    la = len(int_a)
    lb = len(int_b)
    if la > lb:
        int_b = [0 for i in range(la-lb)] + int_b
        lb = len(int_b)
    else:
        int_a = [0 for i in range(lb-la)] + int_a
        la = len(int_a)
    for i in range(1, la+1):
        curr_bit = (int_a[-i] + int_b[-i] + carry) % 2
        carry = (int_a[-i] + int_b[-i] + carry) / 2
        result.insert(0, str(curr_bit))
    if carry == 1:
        result.insert(0, '1')
    return ''.join(result)

# 87. Next Permutation:
def nextPermutation(num):
    if len(num) <= 1:
        return num
    i = len(num) - 1
    while i > 1 and num[i-1]>= num[i]: # It's >=
        i -= 1
    num = num[:i] + sorted(num[i:])
    if i == 0:
        return num
    j = i
    while j < len(num) and num[i-1] >= num[j]: # again >=
        j += 1
    swap(i-1, j, num)
    return num

def swap(i, j, num):
    tmp = num[i]
    num[i] = num[j]
    num[j] = tmp

"""
Wrong answer, this not sorting the rest list
def next_perm(list):
    l = len(list)
    for i in range(1, l):
        for j in range(i+1, l+1):
            if list[-i] > list[-j]:
                tmp = list[-i]
                list[-i] = list[-j]
                list[-j] = tmp
                return list
    return list[::-1]
"""

# 88. Permutations II
# First redo the permutation_i
# Pay attention to this!!!! len(a) == 0 != a is None

def perm_i(list):
    if len(list) == 0:
        return [[]]
    res = []
    for i, e in enumerate(list):
        rest = list[:i] + list[i+1:]
        rest_perm = perm_i(rest)
        for perm in rest_perm:
            res.append( [e,] + perm)
    return res

# Nothing much diff. But use a dict to note which ones are used
def permutations_ii(list):
    d = {}
    def perm_ii(list):
        if len(list) == 0:
            return [[]]
        res = []
        for i, e in enumerate(list):
            if e in d:
                continue
            else:
                d[e] = True
            rest = list[:i] + list[i+1:]
            rest_perm = perm_i(rest)
            for perm in rest_perm:
                res.append( [e,] + perm)
        return res
    return perm_ii(list)

# 89. Remove Duplicates from Sorted List II
# So many traps. Need to remember to set unused.next = None
def remove_dup_from_list_ii(head):
    prev = head
    current = head.next
    unique_head = None
    last = None
    while current is not None:
        if prev.data == current.data:
            while current is not None and current.data == prev.data:
                current = current.next
            if current is not None:
                prev = current
                current = current.next
        else:
            if unique_head is None:
                unique_head = prev
                last = prev
            else:
                last.next = prev
                last = last.next
                last.next = None
            prev = current
            current = current.next
    return unique_head

# 90. Insertion Sort List
# Sister is too niubi
# Inpired by the dummy here
def insertion_sort_list(head):
    dummy = Node(0)
    dummy.next = head
    current = head
    while current.next is not None:
        if current.next.data >= current.data:
            current = current.next
        else:
            insert(dummy, current, current.next)
    return dummy.next

def insert(dummy, tail, node):
    current = dummy
    while node.data > current.nextdata:
        current = current.next
    tail.next = node.next
    node.next = current.next
    current.next = node

# 91. Edit Distance
# Same to the C anwser, need to understand the meaning of M, N, also the boundary
def edit_distance(word1, word2):
    M = len(word1)
    N = len(word2)
    dp= [ [None for i in range(M+1)] for j in range(N+1)]
    for j in range(N+1):
        dp[j][0] = j
    for i in range(M+1):
        dp[0][i] = i
    for j in range(1, N+1):
        for i in range(1, M+1):
            if word1[i-1] == word2[j-1]:
                dp[j][i] = dp[j-1][i-1]
            else:
                dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
    return dp[N][M]

# 92. Reverse Nodes in k-Group
# Remember the way to play the list node
def reverse_nodes_in_k(head, k):
    dummy = Node(0)
    dummy.next = head
    length = get_len(head)
    reverse_time = lenght / k
    ins = dummy
    current = head
    while reverse_time > 0:
        for i in range(k-1):
            move = current.next
            current.next = move.next
            move.next = current
            ins.next = move
        ins = current
        current = current.next
        reverse_time -= 1
    return dummy.next

def get_len(head):
    len = 0
    while head is not None:
        head = head.next
        len += 1
    return len


# 93. Gas Station
# Couldn't understand
def gas_station(gas,cost):
    N = len(gas)
    diff = []
    for i in range(N):
        diff.append(gas[i]-cost[i])
    sum = 0
    startnode = 0
    left_gas = 0
    for i in range(0, N):
        left_gas += diff[i]
        sum += diff[i]
        if sum < 0:
            start_node = i+1
            sum = 0
    if left_gas < 0:
        return -1
    else:
        return start_node

# 94. Combination Sum II
# Fucking moji
def comb_sum_ii(list, target):
    ret = []
    N = len(list)
    sorted(list)
    def comb_sum_helper(i, target, result):
        if target < 0:
            return
        elif target == 0:
            ret.append(result[:])
        for j in range(i,N):
            if j<N-1 and list[j+1] == list[j]:
                continue
            result.append(list[j])
            comb_sum_helper(j+1, target-list[j], result)
            result.pop()
    comb_sum_helper(0, target, [])
    return ret

# 95. Distinct Subsequences
# Need a better understanding in DP
def distinct_subs(S, T):
    len(S) = M
    len(T) = N
    dp = [ [0 for i in range(M+1)] for j in range(N+1)]
    dp[0][0] = 1
    for j in range(N+1):
        dp[j][0] = 1
    for i in range(M+1):
        dp[0][j] = 1
    for i in range(1, M+1):
        for j in range(1, N+1):
            if S[j-1] == T[i-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[M][Nx]

# Why not this?
def distinct_subs(S, T):
    result = 0
    def distinct_helper(T):
        if len(T) == 0:
            return
        if T in S:
            result += 1
        for i, char in enumerate(T):
            distinct_helper(T[:i]+T[i+1:])
    return distinct_helper(T)

# 96. Jump Game II
# Using a dp way, but there's simpler way without dp
def jump_game_ii(jump_list):
    start = 0
    N = len(jump_list)
    step = [100 for i in range(N)]
    step[0] = 1
    while start < N:
        if start + jump_list[start]+1:
                return step[start] + 1
        for i in range(start+1, start + jump_list[start]+1):
            if i >= N-1:
                return 'Will not reach end'
            step[i] = min(step[i], step[start]+1)
        start += 1
    return step[N-1]

# Greedy algorithm. Almost the same. But dp is easier to think but with a O(n) list
def jump_game_ii(jump_list):
    N = len(jump_list)
    start =0
    res = 0
    while start < N-1:
        res += 1
        mx = start
        if start + jump_list[start] >= N-1:
            return res
        for i in range(start+1, start+jump_list[start]+1):
            if i + jump_list[i] > mx + jump_list[mx]:
                mx = i
        start = mx

# 97. Merge k Sorted Lists
def merge_k_sorted_lists(lists):
    dummy = Node(0)
    current = dummy
    q = PriorityQueue()
    for head in lists:
        if head is not None:
            q.push(head)
    while len(q) > 0:
        node = q.top()
        current = current.next = node
        if node.next is not None:
            q.push(node.next)

    return dummy.next

# 98. Zigzag Conversion
# Best result. Remember it's if if if but not if elif ...
def zigzag_convert(str, n):
    result = []
    zig = 2*n - 2
    N = len(str)
    for i in range(n):
        j = 0
        while True:
            if i > 0 and i < n-1 and j-i > 0 and j-i < N:
                result.append(str[j-i])
            if j+1 >0 and j+i < N:
                result.append(str[j+i])
            if j+i > N:
                break
            j += zig
    return ''.join(result)

# my stupid way
def zigzag_convert(str, n):
    result = []
    zig = 2*n - 2
    N = len(str)
    for i in range(n):
        j = 0
        red_index = 0
        while red_index < N:
            red_index = j*zig + i
            if red_index < N:
                result.append(str[red_index])
                j += 1
            else:
                break
            if i == 0 or i == n-1:
                continue
            green_index = j*zig - i
            if green_index > 0 and green_index < N:
                result.append(str[green_index])
    return ''.join(result)

# 99. Anagrams
# Main Idea is to sort and then check each one's letters
def anagrams(list):
    d = {}
    for s in list:
        key = ''.join(sorted(s))
        d.setdefault(key,[]).append(s)
    for key in d:
        if len(d[key]) > 1:
            return d[key]

# 100. Add Two Numbers
# Slim version
def add_two_num(l1, l2):
    carry = 0
    dummy = Node(0)
    current = dummy
    while l1 is not None or l2 is not None or carry != 0:
        sum = carry
        if l1 is not None:
            sum += l1.data
            l1 = l1.next
        if l2 is not None:
            sum += l2.data
            l2 = l2.next
        carry = sum / 10
        sum = sum % 10
        current.next = Node(sum)
        currnet = current.next
    return dummy.next

# dummy version
def add_two_num(l1, l2):
    carry = 0
    dummy = Node(0)
    current = dummy
    while True:
        if l1 is not None and l2 is not None:
            digit = (l1.data + l2.data + carry) % 10
            carry = (l1.data + l2.data + carry) / 10
            l1 = l1.next
            l2 = l2.next
        elif l1 is None:
            digit = (l2.data+carry) % 10
            carry = (l2.data+carry) / 10
            l2 = l2.next
        elif l2 is None:
            digit = (l1.data+carry) % 10
            carry = (l1.data+carry) / 10
            l1 = l1.next
        elif carry != 0:
            digit = carry
            carry = 0
        else:
            break
        current.next = Node(digit)
        current = current.next
    return dummy.next

# 101. Longest Substring Without Repeating Characters
def longest_substring(str):
    d = {}
    max_len = 0
    current = 0
    for i, c in enumerate(str):
        if c not in d:
            d[c] = True
            current += 1
            max_len = max(current, max_len)
        else:
            d = { c : True }
            current = 1
    return max_len

# 102. Recover Binary Search Tree
# Way to think it
def recover_best(root):
    Node1 = None
    Node2 = None
    prev = None
    recover_bst_helper(root, Node1, Node2, prev)
    swap(Node1, Node2)
    return root

def recover_bst_helper(root, Node1, Node2, prev):
    if root is None:
        return
    recover_bst(root.left, Node1, Node2, prev)
    if prev is not None and current.data < prev.data:
        if Node1 is None:
            Node1 = prev
        else:
            Node2 = current
    prev = current
    recover_bst_helper(root.right, Node1, Node2, prev)


# 103. Copy List with Random Pointer
# Not correct
def copy_list(head):
    pass


# 104. Best Time to Buy and Sell Stock III
# see 33

# 105. Valid Palindrome
# Too dan teng
def valid_palin(str):
    start = 0
    end = len(str) - 1
    while start < end:
        while start < end and not str[start].isalnum():
            start += 1
        while start < end and not str[end].isalnum():
            end -= 1
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True


# 106. First Missing Positive
# Not done yet
def first_missing_poisitve(num_list):
    start = 0
    end = len(num_list) - 1
    while start < end:
        if num_list!=


# 107. Rotate List
def rotate_list(head, k):
    dummy = Node(0)
    fast = head
    for i in range(k):
        fast = fast.next
    slow = head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    fast.next = dummy.next
    dummy.next = slow.next
    slow.next = None
    return dummy.next

# 108. Scramble String
def scramble_str(s1, s2):
    if len(s1) != len(s2):
        return False
    return sramble(s1, s2)

def scramble(s1, s2):
    if not has_same_letter(s1, s2):
        return False
    if len(s1) == 0 or len(s1) == 1:
        return True
    for i in range(len(s1)+1):
        if scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:]) or scramble(s1[:i], s2[i:]) and scramble(s1[i:], s2[:i]):
            return True
    return False

def has_same_letter(s1, s2):
    d = {}
    for char in s1:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    for char in s2:
        if char not in d:
            return False
        if d[char] == 1:
            d.pop(char,None)
    if len(d) > 0 :
        return Fasle
    else:
        return True

# 109. 4Sum
def four_sum(s, target):
    ret = []
    if len(s) < 4:
        return
    four_sum_helper(s, target, [], ret)
    return ret

def four_sum_helper(s, target, res, ret):
    if target == 0 and len(res) == 4:
        ret.append(res[:])
        return
    elif len(res) == 4 or len(s) < 4-len(res):
        return
    for i, num in enumerate(s):
        res.append(num)
        four_sum_helper(s[i+1:], target-num, res, ret)
        res.pop()

# 110. Sqrt(x)
def sqrt(x):
    import sys
    start = 0
    end = int(sys.maxint ** 0.5) + 1    # Remember here need to force **0.5 as a integer. Also +1
    while start <= end:                 # maybe for fully test
        mid = (start+end) / 2
        sqr = mid*mid
        if sqr == x:
            return mid
        elif sqr < x:
            start = mid+1
        else:
            end = mid -1
    return (start+end) / 2

# 111. Permutation Sequence
# Way to think:
# 1 2 3      Group them by first digit 1, 2, 3,
# 1 3 2      Will see that (n-1)! is the permutation times of n-1 digits.
# 2 1 3      k / (n-1)! is the bucket that n digit in, which is the sequence of available nums[].
# 2 3 1      Or that is to say, it is the (n-1)! permuation times we loop through the nums
# 3 1 2      So every time we get a num from nums, we need to pop it.
# 3 2 1      nums[] has two important attributes:
#            1. means the available nums we have. 2. Sequence, the order of the nums.
#            So we can change the nums to whatever we want, or even use reverse order.
def perm_seq(n, k):
    num = []
    res = ''
    total = 1
    for i in range(1, n+1):             # n+1
        num.append(str(i))
        total *= i
    k -= 1                              # This is important
    while n > 0:
        total /= n
        i = k / total
        k %= total
        res += num[i]
        num.pop(i)
        n -= 1
    return res                          # return ''.join(res) ?? why not just return res
# Used for testing
# print 'Start: n = ', n,', i = ', i, ', k = ', k,', total = ', total, ', res = ', res, ', num = ', num
# print 'n = ', n,', i = ', i, ', k = ', k,', total = ', total, ', res = ', res, ', num = ', num

# 112. Clone Graph
# Don't know why didn't pass
def cloneGraph(self, node):
    if node is None:
        return None
    # Use oldNode as the oldGraph, newNode as the newGraph. Use tuple (oldNode, newNode) to store relation
    newNodeHead = UndirectedGraphNode(node.label)
    queue = collections.deque()
    queue.append((node,newNodeHead))
    map_dict = {}
    while len(queue) > 0:
        (oldNode,newNode) = queue.popleft()
        if oldNode in map_dict:
            continue
        map_dict[oldNode] = 'Visited'
        newNode.neighbors = []
        for oldNeighbor in oldNode.neighbors:
            newNeighbor = UndirectedGraphNode(oldNeighbor.label)
            queue.append((oldNeighbor, newNeighbor))
            newNode.neighbors.append(newNeighbor)
    return newNodeHead

# 113. Maximal Rectangle
def max_rec():
    pass

# 114. Implement strStr()
def strstr(haystack, needle):
    N = len(haystack)
    H = len(needle)
    while True:
        startStack = 0
        startNeedle = 0
        while haystack[startStack] == needle[startNeedle] and startNeedle < H:
            startStack += 1
            startNeedle += 1
        if startNeedle == H:
            return haystack
        if startStack == N:
            return None
    return None

# KMP way
def strStr(haystack, needle):
    if len(needle) == 0:
        return None
    start = 0
    H = len(haystack)
    N = len(needle)
    while True:
        if H - start < N:
            return None
        if haystack[start] == needle[0]:
            tmp_start = None
            i = 1
            while i < N and heystack[start+i] == needle[i]:
                if tmp_start is None and heystack[start+i] == needle[0]:
                    temp_start = start + i
                i += 1
            if i == N -1:
                return haystack
            if tmp_start is not None:
                start = tmp_start - 1
        start += 1

# 115. Longest Palindromic Substring
# Check each point, has aba and abba two possibilities.
# O(N2) time and O(1) space
def longest_palin_str(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    N = len(s)
    longest = 1
    for i in range(N-1):
        string1 = expand_palin(s, i, i)
        longest = max(longest, len(string1))
        string2 = expand_palin(s, i, i+1)
        longest = max(longest, len(string2))
    return longest

def expand_palin(s, l, r):
    while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


# 116. Sudoku Solver
def sudoku_solver(board):
    solver(board, 0, 0)

def solver(board, row, col):
    (crow, ccol) = getNextEmpty(board, row, col)
    if (crow) == 9:
        return True
    available_num = getAvailable(board, crow, ccol)
    for num in available_num:
        board[crow][ccol] = num
        if solver(board, crow, ccol):
            return True
    board[crow][ccol] = '.'
    return False

def getNextEmpty(board, row, col):
    while row < 9 and board[row][col] != '.':
        if col+1 == 9:
            row = row + 1
        col = (col+1) % 9               # No need to check the last one in the row
    return (row, col)

def getAvailable(board, row, col):
    occupied = []
    for i in range(9):
        if board[row][i] != '.':
            occupied.append(board[row][i])
        if board[i][col] != '.':
            occupied.append(board[i][col])
        box_row = (row/3)*3 + i/3       # This is a awesome algorithm to generate 3 by 3 from 9
        box_col = (col/3)*3 + i%3       # But it's the same to generate from box_row + range(3)
        if board[box_row][box_col] != '.':
                available.append(board[box_row][box_col])
    return available

# 117. Largest Rectangle in Histogram
# O(n2) way to do this
def lar_rec_histo(histo):
    N = len(histo)
    maxV = 0
    for i in range(N):
        if i < N-1 and histo[i] < histo[i+1]:
            continue
        min_height = histo[i]
        for j in range(i-1,-1,-1):
            min_height = min(histo[j], min_height)
            maxV = max( min_height * (i-j+1), maxV)
    return maxV

def lar_rec_histo(histo):
    pass
# KAN BU DONG

# 118. Spiral Matrix
# Need to check the diff in the future
def spiral_matrix(matrix):
    imin = 0
    imax = len(matrix) - 1
    jmin = 0
    jmax = len(matrix[0]) - 1
    res = []
    while True:
        for j in range(jmin, jmax+1):
           res.append(matrix[imin][j])
        imin += 1
        if imin >= imax:
            break

        for i in range(imin, imax+1):
            res.append(matrix[i][jmax])
        jmax -= 1
        if jmin >= jmax:
            break

        for j in range(jmax, jmin-1, -1):
            res.append(matrix[imax][j])
        imax -= 1
        if imin >= imax:
            break

        for i in range(imax, imin-1):
            res.append(matrix[i][jmin])
        jmin += 1
        if jmin >= jmax:
            break
    return res


# 119. Insert Interval
# No need to do the same thing as website. This is pretty good. Just remember to check the last element
def insert_interval(int_list, insert):
    min_num = insert[0]
    max_num = insert[1]
    res = []
    N = len(int_list)
    appended = False
    for int_pair in int_list[:]:
        if int_pair[1] < min_num:
            res.append(int_pair)
        if int_pair[0] > max_num:
            if not appended:
                res.append([min_num,max_num])
                appended = True
            res.append(int_pair)
        if int_pair[0] <= min_num and int_pair[1] >= min_num:
            min_num = int_pair[0]
            int_list.remove(int_pair)
        if int_pair[0] <= max_num and int_pair[1] >= max_num:
            max_num = int_pair[1]
            int_list.remove(int_pair)
    if not appended:
        res.append([min_num,max_num])
    return res

# 120. Merge Interval
# Tai ji ba jian dan le
def merge_interval(intervals):
    N = len(intervals)
    res = []
    prev_end = intervals[0][1]
    prev = intervals[0]
    for inter in intervals[1:]:
        if inter[0] > prev[1]:
            res.append(prev[:])
            prev = inter
        else:
            prev = [min(prev[0],inter[0]), max(prev[1],inter[1])]
    res.append(prev[:])
    return res

# 121. Word Break
# Return True but not list
# This is O(n2) way, use dp can be less
def word_break(rest_word, diction):
    N = len(rest_word)
    if N == 0:
        return True
    for i in range(1,N+1):
        if rest_word[:i] in diction:
            return word_break_helper(res, rest_word[i:], diction)
    return False


# 122. Restore IP Addresses
def restore_ip(ip):
    ret = []
    restore_ip_helper(ret, [], ip)
    return ret

def restore_ip_helper(ret, res, rest_ip):
    if len(res) == 4 and len(rest_ip) == 0:
        ret.append(res[:])
        return
    if len(res) == 4:
        return
    # Ne need to check this? But this will truely save a lot
    #N = len(res)
    #if len(rest_ip) / 3 > 4-N:
    #    return
    for i in range(len(rest_ip)):       # This is so important, see this error
        num = int(rest_ip[:i+1])        # num =  3 rest_ip =  35 res =  [255, 255, 111, 3] i =  0
        if num == 0 or num > 255:       # num =  35 rest_ip =  35 res =  [255, 255, 111, 35] i =  1
            break                       # num =  35 rest_ip =  35 res =  [255, 255, 111, 35] i =  2
        res.append(num)
        restore_ip_helper(ret, res, rest_ip[i+1:])
        res.pop()
# Used for debug print 'num = ', num, 'rest_ip = ', rest_ip, 'res = ', res, 'i = ', i


# 123. Multiply Strings
def mult_str():
    pass

# 124. Sort List
# Need to take a deeper look into the merge sort
def sort_list(head):
    return sort_linked_list(head, getLength):

def sort_linked_list(head, N):
    if N == 0:
        return None
    if N == 1:
        current = head
        head = head.next
        current.next = None
        return current

    half = N/2
    head1 = sort_linked_list(head, half)
    head2 = sort_linked_list(head, N-half)
    return merge_list(head1, head2)

def merge_list(head1, head2):
    dummy = Node(0)
    current = dummy
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    if head1 is not None:
        current.next = head1
    if head2 is not None:
        current.next = head2
    return dummy.next

def getLenght(head):
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length

# 125. Binary Tree Maximum Path Sum
def bt_max_path_sum(root):
    if root is None:
        return 0
    res = 0
    bt_max_path_helper(root, res)
    return res

def bt_max_path_helper(root, res):
    if root is None:
        return 0
    left = bt_max_path_helper(root.left, res)
    right = bt_max_path_helper(root.right, res)
    cur = root.data
    sum = max(max(left, right) + root.data, root.data)
    res = max(res, sum)
    res = max(res, root.data+left+right) # The case that node from left to right is the largest
    return sum                          # This point's max

# 126. Reorder List
def reorder_list():
    pass

# 127. Regular Expression Matching
def regex_matching():
    pass

# 128. Word Search
def word_search():
    pass

# 129. Simplify Path
def simplify_path():
    pass

# 130. Evaluate Reverse Polish Notation
def evalu_reverse_pon():
    pass

# 131. Longest Valid Parentheses
def longest_valid_parentheses():
    pass

# 132. Two Sum
def two_sum():
    pass

# 133. Interleaving String
def interleaving_string():
    pass

# 134. Substring With Concatenation of All Words
def sub_with_con_all_words():
    pass

# 135. Candy
def candy():
    pass

# 136. PalinDrome Partitioning II
def palin_partition_ii():
    pass

# 137. Minimum Window Substring
def min_window_sub():
    pass

# 138. Word Ladder
def word_ladder():
    pass

# 139. Median of Two Sorted Arrays
def med_of_two_arrarys():
    pass

# 140. 3 Sum
def three_sum():
    pass

# 141. Decode Ways
def decode_ways():
    pass

# 142. Divide Two Integers
def divide_two_integers():
    pass

# 143. Word Break II
def word_break_ii():
    pass

# 144. String to Integer (atoi):
def atoi():
    pass

# 145. Surrounded Regions
def surrounded_regions():
    pass

# 146. Text Justification
def text_justi():
    pass

# 147. Reverse Words in a String
# Using python is too simple
def reverse_words_in_str(str):
    return ' '.join(str.split()[::-1])

def reverse_words_in_str(str):
    res = ''
    word = ''
    for char in str:
        if char != ' ':
            word += char
        elif len(word) > 0:
            if res != '':
                res = ' ' + res
            res = word + res
            word = ''
    if len(word) > 0:
        if res != '':
            res = ' ' + res
        res = word + res
    return res

# 148. LRU Cache
def lru_cache():
    pass

# 149. Wildcard Matching
def wildcard_matching():
    pass

# 150. Valid Number
def valid_number():
    pass

# 151. Max Points on a Line
def max_points_line():
    pass

# 152. Word Ladder II
def word_ladder_ii():
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

Not Understand yet:
16. Single Number II
19. Merge Sorted List
27. GrayCode

Not Done yet:
103 Copy List with Random Pointer
113 and 117 Both Rec Graph
123 Multiply Strings

"""
