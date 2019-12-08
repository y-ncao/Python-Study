"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        ret = []
        self.restoreIpAddresses_helper(s, [], ret)
        return ret

    def restoreIpAddresses_helper(self, s, res, ret):
        if len(res) == 4 and len(s) == 0:
            ret.append('.'.join(res))
        if len(res) >= 4 or len(s) == 0:
            return

        for i in range(1, min(3,len(s))+1):
            if ( 0 <= int(s[:i]) < 256 and s[:i][0]!= '0' ) or ( int(s[:i]) == 0 and len(s[:i]) == 1):
                res.append(s[:i])
                self.restoreIpAddresses_helper(s[i:], res, ret)
                res.pop()

        # Note the check:
        # 1. 0<= ip < 255
        # 2. ip shouldn't like 001, 000
