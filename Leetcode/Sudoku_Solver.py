"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solve(board, 0, 0)

    def solve(self, board, i, j):
        i, j = self.getEmpty(board, i, j)
        if i == 9:                      # Set end point
            return True                 # These return valuse are very important
        fill = self.getPossibleInput(board, i, j)
        for f in fill:
            board[i] = board[i][:j] + [f] + board[i][j+1:] # Python string is imutable, but this is weird
            if self.solve(board, i, j):                    # in leetcode, don't know what is their input
                return True
        board[i] = board[i][:j] + ['.'] + board[i][j+1:]
        return False

    def getEmpty(self, board, i, j):
        while i < 9 and j < 9 and board[i][j] != '.':
            i += (j+1) / 9                  # This is so qiao miao
            j = (j+1) % 9
        return (i, j)

    def getPossibleInput(self, board, x, y):
        fill = [str(i+1) for i in range(9)] # Note the type here
        for i in range(9):
            if board[x][i] in fill:
                fill.remove(board[x][i])
            if board[i][y] in fill:
                fill.remove(board[i][y])
        start_x = x / 3 * 3
        start_y = y / 3 * 3
        for i in range(3):
            for j in range(3):
                if board[start_x+i][start_y+j] in fill:
                    fill.remove(board[start_x+i][start_y+j])
        return fill
