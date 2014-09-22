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
            return self.isNumberwoE_2(s.split('e')[0]) and self.isNumberwoE_2(s.split('e')[1], False)
        elif 'E' in s:
            return self.isNumberwoE_2(s.split('E')[0]) and self.isNumberwoE_2(s.split('E')[1], False)
        else:
            return self.isNumberwoE_2(s)

    def isNumberwoE_1(self, s, allow_digit = True):
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

    def isNumberwoE_2(self, s, allow_digit = True):
        digit = '0123456789'
        has_num = False
        for i, char in enumerate(s):
            if i == 0 and char in ['+', '-']:
                continue
            if char == '.' and allow_digit:
                allow_digit = False
                if (i == 0 or s[i-1] in digit) or (i == len(s)-1 or s[i+1] in digit):
                    continue
            if char in digit:
                has_num = True
                continue
            return False
        return has_num

    # Note:
    # 1. Before/after e/E must be a valid num
    # 2. check each sign and dot and num and space
    # 3. Keep an eye on line 44 and line 61 using and / or. Reason is +.8 is valid.
    # 4. isNumberwoE_2 is easier to think, don't think reversely

    # Steps:
    # 1. Strip white space
    # 2. Check if multiple E/e, split by E/e
    # 3. Check each part of num if they are valid with/wo digit
    # 4. Things that can pass:
    #    i.   i == 0 and char in ['+', '-']
    #    ii.  char.isdigit(), pass and set hasNum = True
    #    iii. char == '.': need to check if allow_digit and
    #         check (s[i-1].isdigit() or i == 0) or (i == len(s) - 1 or s[i+1].isdigit())
    #    Set all the rest cases to False
