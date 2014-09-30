#!/usr/bin/env python

file_name = 'Text_Justification'
func_name = 'fullJustify'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(["What","must","be","shall","be."], 12)
