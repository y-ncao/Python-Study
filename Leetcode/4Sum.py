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
        return self.fourSum_1(num, target)

    # This is kitt's way, using dictionary
    def fourSum_1(self, num, target):
        numLen, res, d = len(num), set(), {}
        if numLen < 4: return []
        num.sort()
        for p in xrange(numLen):
            for q in xrange(p + 1, numLen):
                if num[p] + num[q] not in d:
                    d[ num[p] + num[q] ] = [(p,q)]
                else:
                    d[ num[p] + num[q] ].append( (p,q) )
        for i in xrange(numLen):
            for j in xrange(i + 1, numLen - 2):
                T = target - num[i] - num[j]
                if T in d:
                    for k in d[T]:
                        if k[0] > j: res.add( ( num[i], num[j], num[k[0]], num[k[1]] ) )
        return [ list(i) for i in res ]

    # Won't pass because this is O(n^3)
    def fourSum_2(self, num, target):
        num.sort()
        N = len(num)
        ret = []
        for i in range(N-3):
            if i > 0 and num[i] == num[i-1]:
                continue
            for j in range(i+1, N-2):
                if j > i+1 and num[j] == num[j-1]:
                    continue
                l = j + 1
                r = N - 1
                while l < r:
                    sum = num[i] + num[j] + num[l] + num[r] < target
                    if sum < target:
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        ret.append([num[i], num[j], num[l], num[r]])
                        l += 1
                        r -= 1
                        while l < r and num[l] == num[l-1]:
                            l += 1
                        while l < r and num[r] == num[r+1]:
                            r -= 1
        return ret
