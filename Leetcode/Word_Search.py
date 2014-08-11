"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        rowN = len(board)
        colN = len(board[0])
        visited = [ [False for j in range(colN)] for i in range(rowN) ]
        for i in range(rowN):
            for j in range(colN):
                if self.isWord(board, visited, i, j, word):
                    return True
        return False

    def isWord(self, board, visited, i, j, word):
        if len(word) == 0:
            return True
        rowN = len(board)
        colN = len(board[0])
        if i < 0 or i >= rowN or j < 0 or j >= colN or visited[i][j] or board[i][j] != word[0]:
            return False

        visited[i][j] = True
        if self.isWord(board, visited, i+1, j, word[1:]) or self.isWord(board, visited, i-1, j, word[1:]) or self.isWord(board, visited, i, j+1, word[1:]) or self.isWord(board, visited, i, j-1, word[1:]):
            return True

        visited[i][j] = False

        return False
