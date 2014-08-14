#!/usr/bin/env python

file_name = 'Longest_Valid_Parentheses'
func_name = 'longestValidParentheses'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(")()())")
