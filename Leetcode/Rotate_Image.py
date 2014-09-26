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
        start = 0
        end = len(matrix) - 1
        while start < end:
            for i in range(end-start):
                tmp = matrix[start][start+i]
                matrix[start][start+i] = matrix[end-i][start]
                matrix[end-i][start] = matrix[end][end-i]
                matrix[end][end-i] = matrix[start+i][end]
                matrix[start+i][end] = tmp
                #print matrix
            start += 1
            end -= 1
        return matrix

    # Note:
    # 1. Remember line 17, which is end-start

    """
    matrix = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
    def rotate(matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
    print rotate(matrix)
    """
