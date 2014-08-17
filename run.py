#!/usr/bin/env python

file_name = 'Minimum_Window_Substring'
func_name = 'minWindow'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("ADOBECODEBANC", 'ABC')
