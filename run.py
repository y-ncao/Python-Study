#!/usr/bin/env python

file_name = 'Median_of_Two_Sorted_Arrays'
func_name = 'findMedianSortedArrays'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([1,2],[1,2])
