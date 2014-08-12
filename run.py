#!/usr/bin/env python

file_name = 'Decode_Ways'
func_name = 'numDecodings'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)('12')
