
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        N = len(num)
        for i in range(N)[::-1]:
            if num[i-1] < num[i]:
                for j in range(i-1, N)[::-1]:
                    if num[i-1] < num[j]:
                        return self.find_next(i-1, j, num)
        num.reverse()
        return num

    def find_next(self, i, j, num):
        num[i], num[j] = num[j], num[i]
        return num[:i+1] + sorted(num[i+1:])

    # Way to think:
    # [7, 8, 6, 9, 8, 7, 2] ->
    #        |        |
    # 1. Find 6 first
    # 2. Find 7
    # 3. Swap 6 and 7, sort all the nums after 6
    
    # Steps
    # 1. Iterate from the back to the front, find the first element that A[i-1] < A[i]
    # 2. Iterate from the back to the front, find the first element that A[j] > A[i-1]
    # 3. swap A[i-1] and A[j], return A[:i+1] + sorted(A[i+1:])
