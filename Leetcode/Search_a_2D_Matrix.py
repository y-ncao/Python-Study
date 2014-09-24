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
        M = len(matrix)
        N = len(matrix[0])
        start = 0
        end = M*N - 1
        while start <= end:
            mid = (start+end) / 2
            i = mid / N
            j = mid % N
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

```
#####Search a 2D Matrix II
What if we allow duplicate in the matrix and need to find out all the posisitons
```

def search_matrix_II(matrix, target):
    lb = search_for_bound(matrix, target, True)
    if lb == -1:
        return False
    rb = search_for_bound(matrix, target, False)
    res = []
    for i in range(lb, rb+1):
        res.append((i/N, i%N))
    return res

def search_for_bound(matrix, target, is_lower_bound):
    M = len(matrix)
    N = len(matrix[0])
    start = 0
    end = M*N - 1
    while start + 1 < end:
        mid = (start+end) / 2
        if matrix[mid/N][mid%N] == target:
            if is_lower_bound:
                end = mid
            else:
                start = mid
        elif matrix[mid/N][mid%N] < target:
            start = mid
        else:
            end = mid

    if is_lower_bound:
        if matrix[start/N][start%N] == target:
            return start
        elif matrix[end/N][end%N] == target:
            return end
    else:
        if matrix[end/N][end%N] == target:
            return end
        elif matrix[start/N][start%N] == target:
            return start

    return -1

```
Note:
1. from [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32775405.html) that answer check mid-1 == mid
2. I don't think this is a good way. So need to discuss here.
```
