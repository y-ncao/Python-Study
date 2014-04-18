#!/usr/bin/env python

# 1.Single Number
# Fuck!!! use XOR

# 2. Maximum depth of binary tree
def maximum_depth(root):
    if root is None:
        return 0

    return max( maximum_depth(root.left), maximum_depth(root.right)) + 1
