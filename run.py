#!/usr/bin/env python

file_name = '3Sum_Closest'
func_name = 'threeSumClosest'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)()
