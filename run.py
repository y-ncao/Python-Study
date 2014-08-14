#!/usr/bin/env python

file_name = 'Valid_Number'
func_name = 'isNumber'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("32.e-80123")
