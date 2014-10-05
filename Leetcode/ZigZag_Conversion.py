"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:    # Be careful about nRows ==1
            return s
        size = 2 * nRows - 2
        n = len(s) / size + 1
        res = []
        for i in range(size):
            if i == 0 or i == size / 2:
                for j in range(n):
                    if j * size + i < len(s):
                        res.append(s[j*size+i])
                if i == size/2:
                    return ''.join(res)
            else:
                for j in range(n):
                    if j * size + i < len(s):
                        res.append(s[j*size+i])
                    if (j+1) * size - i < len(s):
                        res.append(s[(j+1) * size - i])
