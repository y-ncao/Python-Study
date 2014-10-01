#!/usr/bin/env python

file_name = 'Wildcard_Matching'
func_name = 'isMatch'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("caab", "c*abb")
