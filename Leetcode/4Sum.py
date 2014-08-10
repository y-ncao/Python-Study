"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num, target = ([1,0,-1,0,-2,2], 0)
        num = sorted(num)
        N = len(num)
        ret = []
        if N <= 4:
            return ret
        for i in range(N-3):
            if i > 0 and num[i] == num[i-1]:
                continue
            for j in range(i+1, N-2):
                if j > i and num[j] == num[j-1]:
                    continue
                for k in range(j+1, N-1):
                    if k > j and num[k] == num[k-1]:
                        continue
                    for l in range(k+1, N):
                        if
                        if num[i] + num[j] + num[k] + num[l] == target:
                            ret.append([num[i], num[j], num[k], num[l]])
        #print ret
        return ret
