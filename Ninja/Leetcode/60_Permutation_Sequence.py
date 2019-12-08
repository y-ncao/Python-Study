"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        num_list = []
        total = 1
        res = ''
        for i in range(1, n+1):         # Detail!!! this is n+1
            total *= i
            num_list.append(str(i))
        k -= 1                          # This is very important
        while n > 0:
            total /= n
            i = k / total
            k %= total
            res += num_list[i]
            num_list.pop(i)
            n -= 1
        return res

    # total is very important here
