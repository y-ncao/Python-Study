"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        return self.maxSubArray_2(A)

    def maxSubArray_1(self, A):
        max_sum = A[0]
        cur_sum = 0
        for num in A:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

    # dp way
    # dp[i] = max(A[i], dp[i-1]+A[i])
    # Because we don't need to store dp[i], so simplify to dp
    def maxSubArray_2(self, A):
        res = A[0]
        dp = A[0]
        for num in A[1:]:
            dp = max(num, dp+num)
            res = max(res, dp)
        return res
