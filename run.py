#!/usr/bin/env python

file_name = 'Surrounded_Regions'
func_name = 'solve'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()
#a = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
a = ["O"]
getattr(instance, func_name)(a)
print a
