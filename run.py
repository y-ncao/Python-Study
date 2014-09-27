#!/usr/bin/env python

file_name = 'Count_and_Say'
func_name = 'countAndSay'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(6)
