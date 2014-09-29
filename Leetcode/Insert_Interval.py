"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        inserted = False
        for inter in intervals:
            if newInterval.end < inter.start:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(inter)
            elif inter.end < newInterval.start:
                res.append(inter)
            else:
                newInterval.start = min(newInterval.start, inter.start)
                newInterval.end = max(newInterval.end, inter.end)

        if not inserted:
            res.append(newInterval)
        return res
    # Note
    # 分三种情况讨论
    # 1. 插入区间在当前区间左边 - 如果没插入就插入, 添加当前区间
    # 2. 插入区间在当前区间右边 - 插入当前区间
    # 3. 剩余的mix情况        - 合并两个区间