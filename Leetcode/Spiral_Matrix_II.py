"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ret = [ [ 0 for i in range(n)] for j in range(n)]
        num = 1
        start_row = start_col = 0
        end_row = end_col = n - 1
        while start_row < end_row and start_col < end_col:
            for i in range(start_col, end_col + 1):
                ret[start_row][i] = num
                num += 1
            start_row += 1
            for i in range(start_row, end_row + 1):
                ret[i][end_col] = num
                num += 1
            end_col -= 1
            for i in range(end_col, start_col - 1, -1):
                ret[end_row][i] = num
                num += 1
            end_row -= 1
            for i in range(end_row, start_row -1, -1):
                ret[i][start_col] = num
                num += 1
            start_col += 1
        if n%2 == 1:
            ret[start_col][start_row] = num
        return ret
