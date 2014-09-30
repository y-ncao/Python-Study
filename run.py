#!/usr/bin/env python

file_name = 'Word_Ladder_II'
func_name = 'findLadders'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
