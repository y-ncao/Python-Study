#!/usr/bin/env python

file_name = 'Maximal_Rectangle'
func_name = 'maximalRectangle'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(['00010010','00010010','00010010','00000000','00010010'])
