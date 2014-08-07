#!/usr/bin/env python

file_name = 'Pow_x_n'
func_name = 'pow'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(2.5,2)
