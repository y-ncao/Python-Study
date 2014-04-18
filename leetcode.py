#!/usr/bin/env python

# 1.Single Number
# Fuck!!! use XOR

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

# Reverse Integer
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

if __name__ == '__main__':
    #print reverse_int(131)


# Note for todo:
"""
1. check the best way to implement reverse_int. This is not a clever one
"""
