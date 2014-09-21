#!/usr/bin/env python

file_name = 'Palindrome_Partitioning_II'
func_name = 'minCut'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("bb")
