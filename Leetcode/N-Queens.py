"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

# Need another way to think about this, fill row instead of fill column

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        ret = []
        res = ['.'*n for i in range(n)]
        self.solveNQueens_helper(n, res, ret, 0)
        return ret

    def solveNQueens_helper(self, n, res, ret, queens):
        if queens == n:
            ret.append(res[:])
            return
        for i in range(n):
            new_row = '.'*n
            res[queens] = new_row[:i] + 'Q' + new_row[i+1:]
            if self.is_valid(res, queens, i):
                self.solveNQueens_helper(n, res, ret, queens+1)
            res[queens] = new_row

    def is_valid(self, board, row, col):
        for i in range(row):
            for j in range(len(board[0])):
                if board[i][j] == 'Q' and (j == col or abs(row-i) == abs(col-j)):
                    return False
        return True

# Remember this it's row-i == col-j
