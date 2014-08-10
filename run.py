#!/usr/bin/env python

file_name = 'Two_Sum'
func_name = 'twoSum'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([3,2,4], 6)
