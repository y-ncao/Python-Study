#!/usr/bin/env python

file_name = 'Implement_strStr'
func_name = 'strStr'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("babba", "bbb")
