#!/usr/bin/env python

file_name = 'Evaluate_Reverse_Polish_Notation'
func_name = 'evalRPN'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
