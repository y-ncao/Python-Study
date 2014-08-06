"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        return self.threeSumClosest_1(num, target)

    def threeSumClosest_1(self, num, target):
        N = len(num)
        num = sorted(num)
        ret = num[0]+num[1]+num[2]
        i = 0
        while i < N-2:
            l = i + 1
            r = N - 1
            while l < r:
                threesum = num[i] + num[l] + num[r]
                if abs(threesum-target) < abs(ret-target): # Need to check this before changing threesum
                    ret = threesum
                if threesum == target:
                    return target
                elif threesum < target:
                    l += 1
                else:
                    r -= 1
            i += 1
            while i < N-2 and num[i] == num[i-1]: # This will save some calculation
                i += 1
        return ret

    # time exceeded
    def threeSumClosest_2(self, num, target):
        N = len(num)
        if N < 3:
            return 0
        closest_sum = num[0]+num[1]+num[2]
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    sum = num[i] + num[j] + num[k]
                    if sum == target:
                        return target
                    elif abs(target-sum) < abs(closest_sum):
                        closest_sum = sum
        return closest_sum
