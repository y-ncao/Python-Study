#!/usr/bin/env python

file_name = 'Divide_Two_Integers'
func_name = 'divide'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(29, 4)
