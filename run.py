#!/usr/bin/env python

file_name = 'Interleaving_String'
func_name = 'isInterleave'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("aabcc","dbbca","aadbbbaccc")
