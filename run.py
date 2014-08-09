#!/usr/bin/env python

file_name = 'First_Missing_Positive'
func_name = 'firstMissingPositive'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([1,1])
