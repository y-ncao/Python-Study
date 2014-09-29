
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3  1,3,2
3,2,1  1,2,3
1,1,5  1,5,1
"""

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation_1(self, num):
        if len(num) <= 1:
            return num
        i = len(num) - 1
        while i > 0 and num[i-1]>= num[i]: # It's >=
            i -= 1
        num = num[:i] + sorted(num[i:])
        if i == 0:
            return num
        j = i
        while j < len(num) and num[i-1] >= num[j]: # again >=
            j += 1
        self.swap(i-1, j, num)
        return num

    def swap(self, i, j, num):
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp

    # A little bit hard to think
    def nextPermutation(self, num):
        N = len(num)
        for i in range(N)[::-1]:
            for j in range(i)[::-1]:
                if num[i] > num[j]:
                    return self.find_next(i, j, num)
        return num.reverse()
        
    def find_next(self, i, j, num):
        ret = []
        ret.extend(num[:j])
        ret.append(num[i])
        ret.extend(sorted(num[j:i]))
        return ret