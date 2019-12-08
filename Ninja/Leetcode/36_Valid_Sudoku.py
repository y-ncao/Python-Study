"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in row:
                    row.append(board[i][j])
                elif board[i][j] in row:
                    return False
                if board[j][i] != '.' and board[j][i] not in col:
                    col.append(board[j][i])
                elif board[j][i] in col:
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                square = []
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] != '.' and board[i+x][j+y] not in square:
                            square.append(board[i+x][j+y])
                        elif board[i+x][j+y] in square:
                            return False
        return True
