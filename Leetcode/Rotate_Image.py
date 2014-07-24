"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return self.rotate_2(matrix)

    def rotate_1(self, matrix):
        n = len(matrix)

        for i in range(n/2):
            start = i
            end   = n-1-i
            for j in range(start, end):
                offset = j - start
                top = matrix[start][j]
                matrix[start][j]          = matrix[end-offset][start]  # bottom to top
                matrix[end-offset][start] = matrix[end][end-offset]    # right to left
                matrix[end][end-offset]   = matrix[j][end]             # top to bottom
                matrix[j][end]            = top
        return matrix

    def rotate_2(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                self.swap(matrix, i, j , j, i)
        for i in range(n):
            for j in range(n/2):
                self.swap(matrix, i, j, i, n-1-j)
        return matrix

    def swap(self, matrix, i1, j1, i2, j2):
        tmp = matrix[i1][j1]
        matrix[i1][j1] = matrix[i2][j2]
        matrix[i2][j2] = tmp
