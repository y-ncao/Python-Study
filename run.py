#!/usr/bin/env python

file_name = 'Word_Break_II'
func_name = 'wordBreak'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("aaaaaaa", ["aaaa","aaa"])
