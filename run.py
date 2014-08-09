#!/usr/bin/env python

file_name = 'Edit_Distance'
func_name = 'minDistance'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)('abcd','abca')
