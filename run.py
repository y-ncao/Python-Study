#!/usr/bin/env python

file_name = 'Next_Permutation'
func_name = 'nextPermutation'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([1,1,3])
