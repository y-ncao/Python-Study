"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_map = { 'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000,
                  }
        ret = 0
        prev = s[0]
        for char in s:
            if roman_map[char] <= roman_map[prev]:
                ret += roman_map[char]
            else:
                ret += roman_map[char] - 2 * roman_map[prev]
            prev = char
        return ret
