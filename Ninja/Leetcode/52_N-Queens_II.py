"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.ret = 0
        self.totalNQueens_helper(n, [])
        return self.ret

    def totalNQueens_helper(self, n, res):
        if len(res) == n:
            self.ret += 1                    # ret.append(res[:])
            return
        for i in range(n):
            res.append(i)
            if self.is_valid(res):
                self.totalNQueens_helper(n, res)
            res.pop()

    def is_valid(self, board):
        l = len(board) - 1
        for i in range(len(board)-1):
            if board[i] == board[l] or abs(board[i]-board[l]) == abs(i-l):
                    return False
        return True

    # First remember this is diff to a normal cheesboard,
    # placing a n*n chess board
    # input 1, expect 1 but not 8
    # Keep in mind the way to use self.ret as global
