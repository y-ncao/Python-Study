#!/usr/bin/env python

file_name = 'Largest_Rectangle_in_Histogram'
func_name = 'largestRectangleArea'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([2,1,5,6,2,3])
