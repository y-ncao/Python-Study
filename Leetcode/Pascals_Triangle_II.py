"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        return self.getRow_2(rowIndex)

    def getRow_1(self, rowIndex):
        ret = [1]
        if rowIndex == 0:
            return ret
        while rowIndex > 0:
            if len(ret) > 1:
                for i in range(1, len(ret)):
                    ret[i-1] = ret[i] + ret[i-1]
            ret.insert(0, 1)
            rowIndex -= 1
        return ret

    def getRow_2(self, rowIndex):
        ret = [1 for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i-1, 0, -1):
                ret[j] += ret[j-1]
        return ret
