"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = sorted(num)
        N = len(num)
        ret = []
        for i in range(N-2):
            if i > 0 and num[i] == num[i-1]:
                continue
            l = i + 1
            r = N - 1
            while l < r:
                if num[i] + num[l] + num[r] < 0:
                    l += 1
                elif num[i] + num[l] + num[r] > 0:
                    r -= 1
                else:
                    ret.append([num[i], num[l], num[r]])
                    l += 1
                    r -= 1
                    while l < r and num[l] == num[l-1]:
                        l += 1
                    while l < r and num[r] == num[r+1]:
                        r -= 1
        return ret

    # Notice:
    # 1. This is almost the same to 3 Sum Closest.
    # 2. remember to remove duplicate result by doing l += 1 and r -= 1, also the continue on line 21
