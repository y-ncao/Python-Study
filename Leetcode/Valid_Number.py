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
        # Need to think:
        # 1. dot
        # 2. e
        # 3. '-'/'+'
        # 4. ' '
        has_dot = False
        has_e = False
        has_sign = False
        has_digit = False
        s = s.strip()
        N = len(s)
        if N == 0:
            return False
        for i, char in enumerate(s):
            if char.isdigit():
                has_digit = True
                continue
            if (char == '-' or char == '+'):
                if not (i == 0 or s[i-1] == 'e'):
                    return False
                elif i == N-1 or s[i+1] == 'e':
                    return False
                else:
                    continue

            if char.isalpha():
                if char != 'e':
                    return False
                else:
                    if (has_e or i == 0 or i == N-1):
                        return False
                    elif (i == 0 or not s[i-1].isdigit()) and (i == N-1 or not s[i+1].isdigit()):
                        return False
                    has_e = True

            if not char.isalnum():
                if char != '.':
                    return False
                else:
                    if has_dot or len(s) == 1 or has_e:
                        return False
                    elif (i == 0 or not s[i-1].isdigit()) and (i == N-1 or not s[i+1].isdigit()):
                        return False
                    has_dot = True
        return has_digit
