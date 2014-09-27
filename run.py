#!/usr/bin/env python

file_name = 'Subsets'
func_name = 'subsets'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([1,2,3])
