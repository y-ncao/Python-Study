"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
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
        for i, n in enumerate(nums):
            if target - n in num_map:
                return (num_map[target - n], i)
            else:
                num_map[n] = i

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
