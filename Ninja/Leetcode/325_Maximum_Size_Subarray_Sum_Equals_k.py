"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Too slow, won't AC
        max_len = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                subarray = nums[i:j]
                if sum(subarray) == k:
                    max_len = max(max_len, j-i)

        return max_len

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_map = {0:0}
        cur_sum = 0
        max_len = 0
        for i, n in enumerate(nums):
            cur_sum += n
            if cur_sum - k in sum_map:
                max_len = max(max_len, i + 1 - sum_map[cur_sum - k])

            if cur_sum not in sum_map:
                sum_map[cur_sum] = i + 1

        return max_len
