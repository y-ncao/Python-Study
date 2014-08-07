#!/usr/bin/env python

file_name = 'Sqrt_x'
func_name = 'sqrt'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(1579205274)
