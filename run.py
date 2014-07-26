#!/usr/bin/env python

import importlib

file_name = 'Subsets'

i = importlib.import_module('Leetcode.%s' % file_name)

a = i.Solution()


print a.subsets([1,2,3,4])
