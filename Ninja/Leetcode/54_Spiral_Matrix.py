"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        M = len(matrix)
        if len(matrix) == 0:
            return []
        N = len(matrix[0])
        start_col = start_row = 0
        end_row   = M - 1
        end_col   = N - 1
        ret = []

        while True:
            for i in range(start_col, end_col + 1):
                ret.append(matrix[start_row][i])
            start_row += 1
            if start_row > end_row:
                break
            for i in range(start_row, end_row + 1):
                ret.append(matrix[i][end_col])
            end_col -= 1
            if start_col > end_col:
                break
            for i in range(start_col, end_col + 1)[::-1]:
                ret.append(matrix[end_row][i])
            end_row -= 1
            if start_row > end_row:
                break
            for i in range(start_row, end_row + 1)[::-1]:
                ret.append(matrix[i][start_col])
            start_col += 1
            if start_col > end_col:
                break
        return ret

    # Note:
    # This way is a lot better to memory
