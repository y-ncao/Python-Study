#!/usr/bin/env python

file_name = 'Add_Binary'
func_name = 'addBinary'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)('11','1')
