"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    # @return a list of lists of integers
    def generate(numRows):
        return self.generate_1(numRows)

    def generate_1(self, numRows):
        res = []
        for j in range(numRows):
            current = [1]
            for i in range(1, j):
                current.append(res[-1][i]+res[-1][i-1])
            if j>=1:
                current.append(1)
            res.append(current[:])
        return res

    def generate_2(self, numRows):
        if numRows ==0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1], [1,1]]
        prev = [1,1]
        for j in range(numRows-1):
            current = [1]
            for i in range(1,len(prev)):
                current.append(prev[i]+prev[i-1])
            current.append(1)
            res.append(current[:])
            prev = current
        return res
