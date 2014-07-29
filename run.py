#!/usr/bin/env python

file_name = 'Unique_Paths_II'
func_name = 'uniquePathsWithObstacles'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([[0]])
