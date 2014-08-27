"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        return self.twoSum_3(num, target)

    # O(n^2)
    def twoSum_1(self, num, target):
        N = len(num)
        for i in range(N-1):
            for j in range(i+1, N):
                if target == num[i] + num[j]:
                    return (num[i], num[j])

    # O(n)
    def twoSum_2(self, num, target):
        num_map = {}
        for i, n in enumerate(num):
            if target - n not in num_map:
                num_map[n] = i
            else:
                return (num_map[target-n] + 1, i + 1) # Don't know why leetcode call the index [0] as 1

    # O(nlgn) This is the best way, used in X Sum
    def twoSum_3(self, num, target):
        d = {}                          # This is used because we need to sort the array
        for i, n in enumerate(num):
            d.setdefault(n, []).append(i+1)
        num = sorted(num)
        l = 0
        r = len(num) - 1
        while l < r:
            if num[l] + num[r]  == target:
                if num[l] == num[r]:
                    return (d[num[l]][0], d[num[r]][1])
                else:
                    return sorted((d[num[l]][0], d[num[r]][0]))
            elif num[l] + num[r] < target:
                l += 1
            else:
                r -= 1

    # Note:
    # 1. Keep in mind we need to use a dict to store the original position.