"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        min_product = A[0]
        max_product = A[0]
        largest_product = A[0]

        for num in A[1:]:
            if num > 0:
                max_product = max(num, num * max_product)
                min_product = min(num, num * min_product)
            else:
                tmp = min_product
                min_product = min(num, num * max_product)
                max_product = max(num, num * tmp)
            largest_product = max(largest_product, max_product)

        return largest_product

    # Notice:
    # 1. Need to remember the idea to flip the result, and keep a note the min and max
    # 2. Be careful on line 21,
    # 3. Check the condition, it's a list of integer, so I was thinking too much
