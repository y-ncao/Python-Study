#!/usr/bin/env python

file_name = 'Maximum_Product_Subarray'
func_name = 'maxProduct'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([-4,-3,-2])
