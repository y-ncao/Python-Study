#!/usr/bin/env python

file_name = 'Restore_IP_Addresses'
func_name = 'restoreIpAddresses'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)("25525511135")
