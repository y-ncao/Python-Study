"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        if len(s.split('e')) > 2 or len(s.split('E')) > 2:
            return False

        if 'e' in s:
            return self.isNumberwoE(s.split('e')[0]) and self.isNumberwoE(s.split('e')[1], False)
        elif 'E' in s:
            return self.isNumberwoE(s.split('E')[0]) and self.isNumberwoE(s.split('E')[1], False)
        else:
            return self.isNumberwoE(s)

    def isNumberwoE(self, s, allow_digit = True):
        digit = '0123456789'
        N = len(s)
        if N == 0:
            return False
        has_digit = False
        has_num = False
        for i, char in enumerate(s):
            if char == '+' or char == '-':
                if i != 0:
                    return False
            elif char == ' ':
                return False
            elif char == '.':
                if not allow_digit or has_digit:
                    return False
                if (i == 0 or s[i-1] not in digit) and (i == N-1 or s[i+1] not in digit):
                    return False
                has_digit = True
            elif char not in digit:
                return False
            else:
                has_num = True
        return has_num

    # Main idea is:
    # 1. Before/after e/E must be a valid num
    # 2. check each sign and dot and num and space
