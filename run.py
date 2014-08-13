#!/usr/bin/env python

file_name = 'Spiral_Matrix'
func_name = 'spiralOrder'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)([[ 1, 2, 3,4,5 ],[ 4, 5, 6 ,7,8],[  8, 9,10,11,12]])
