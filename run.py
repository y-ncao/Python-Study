#!/usr/bin/env python

file_name = 'Substring_with_Concatenation_of_All_Words'
func_name = 'findSubstring'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("aaa", ["a","a"])
