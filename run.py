#!/usr/bin/env python

file_name = 'Minimum_Path_Sum'
func_name = 'minPathSum'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([[1,2,5],[3,2,1]])
