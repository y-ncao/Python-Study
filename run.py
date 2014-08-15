#!/usr/bin/env python

file_name = 'Word_Ladder'
func_name = 'ladderLength'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("a", "c", set(["a","b","c"]))
