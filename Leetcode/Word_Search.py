"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given
```
board = [ ["ABCE"],
          ["SFCS"],
          ["ADEE"]
          ]
```
word = "ABCCED", -> returns true,  
word = "SEE", -> returns true,  
word = "ABCB", -> returns false.
"""

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0] and self.isWord(board, i, j, 0, word):
                    return True
        return False

    def isWord(self, board, i, j, index, word):
        if index == len(word):
            return True

        M = len(board)
        N = len(board[0])

        if i < 0 or i >= M or j < 0 or j >= N or board[i][j] != word[index]:
            return False

        board[i][j] = '#'
        if self.isWord(board, i+1, j, index+1, word) or \
                self.isWord(board, i-1, j, index+1, word) or \
                self.isWord(board, i, j+1, index+1, word) or \
                self.isWord(board, i, j-1, index+1, word):
           return True

        board[i][j] = word[index]

        return False

    # Note:
    # 1. Keep in mind the declare of matrix, M, N, board, board[0]
    # 2. Line 28 check board[i][j] == word[0]
    # 3. Use in place make board[i][j] = '#' and recover later
    # 4. Line 43 line break use \
    # 5. Very important, must remark the 'visisted' part
