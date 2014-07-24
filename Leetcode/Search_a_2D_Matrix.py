"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        start = 0
        end = len(matrix) -1            # -1 !!!
        while start <= end:
            mid = (start + end) / 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                col = mid
                start = 0
                end = len(matrix[0]) -1         # -1!!!
                while start <= end:
                    mid = (start + end) / 2
                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                return False
            elif target < matrix[mid][0]:
                end = mid-1
            else:
                start = mid + 1
        return False

    # This is better, nested matrix
"""
Generate m*n matrix
a = 0
m = []
for i in range(10):
    row = []
    for j in range(8):
        row.append(a)
        a += 1
    m.append(row[:])
"""
