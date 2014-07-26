#!/usr/bin/env python

file_name = 'Pascals_Triangle_II'
func_name = 'getRow'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(4)
