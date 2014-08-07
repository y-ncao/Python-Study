#!/usr/bin/env python

file_name = 'Palindrome_Partitioning'
func_name = 'partition'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("aab")
