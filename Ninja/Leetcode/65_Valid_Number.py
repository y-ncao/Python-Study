"""
Validate if a given string is numeric.

Some examples:
* "0" => true
* " 0.1 " => true
* "abc" => false
* "1 a" => false
* "2e10" => true

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
        has_num = False
        for i, char in enumerate(s):
            if i == 0 and char in ['+', '-']:
                continue
            if char == '.' and allow_digit:
                allow_digit = False
                continue
            if char.isdigit():
                has_num = True
                continue
            return False
        return has_num

    # Note:
    # 1. Strip white space
    # 2. Check if multiple E/e, split by E/e
    # 3. Check each part of num if they are valid with/wo digit
    # 4. Things that can pass:
    #    i.   i == 0 and char in ['+', '-']
    #    ii.  char.isdigit(), pass and set hasNum = True
    #    iii. char == '.': need to check if allow_digit
    #    Set all the rest cases to False
