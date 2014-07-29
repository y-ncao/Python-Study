#!/usr/bin/env python

file_name = 'Longest_Consecutive_Sequence'
func_name = 'longestConsecutive'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([100, 4, 200, 1, 3, 2])
