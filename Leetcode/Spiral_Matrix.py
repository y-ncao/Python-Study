"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].>
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        M = len(matrix)
        if len(matrix) == 0:
            return []
        N = len(matrix[0])
        start_x = 0
        start_y = 0
        end_x   = N - 1
        end_y   = M - 1
        ret = []
        while True:
            for i in range(start_x, end_x + 1):
                ret.append(matrix[start_y][i])
            start_y += 1
            if start_y > end_y:
                break
            for i in range(start_y, end_y + 1):
                ret.append(matrix[i][end_x])
            end_x -= 1
            if start_x > end_x:
                break
            for i in range(start_x, end_x + 1)[::-1]:
                ret.append(matrix[end_y][i])
            end_y -= 1
            if start_y > end_y:
                break
            for i in range(start_y, end_y + 1)[::-1]:
                ret.append(matrix[i][start_x])
            start_x += 1
            if start_x > end_x:
                break
        return ret
