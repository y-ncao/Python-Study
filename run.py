#!/usr/bin/env python

file_name = 'Longest_Substring_Without_Repeating_Characters'
func_name = 'lengthOfLongestSubstring'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("abcdeababbbabcde")
