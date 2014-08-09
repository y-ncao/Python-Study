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
        for i, inter in enumerate(intervals):
            if not inserted and inter.start > newInterval.end:
                res.append(newInterval)
                res.append(inter)
                inserted = True
            elif inter.start > newInterval.end or inter.end < newInterval.start:
                res.append(inter)
            else:
                newInterval.start = min(newInterval.start, inter.start)
                newInterval.end = max(newInterval.end, inter.end)
        if not inserted:
            res.append(newInterval)
        return res

""" This works, but leetcode require a sorted result
    def insert(self, intervals, newInterval):
        res = []
        for i, inter in enumerate(intervals):
            if inter.start > newInterval.end or inter.end < newInterval.start:
                res.append(inter)
                continue
            if newInterval.start >= inter.start and newInterval.start <= inter.end:
                newInterval.start = min(inter.start, newInterval.start)
            if newInterval.end >= inter.start and newInterval.end <= inter.end:
                newInterval.end = max(inter.end, newInterval.end)
        res.append(newInterval)
        return res
"""


""" To complicated
    def insert(self, intervals, newInterval):
        if newInterval.end < intervals[0].start:
            intervals.insert(0, newInterval)
            return intervals
        elif newInterval.start > intervals[-1].end:
            intervals.append(newInterval)
            return intervals
        i = 0
        ret = []
        while i < len(intervals):
            if intervals[i].start <= newInterval.start and intervals[i].end >= newInterval.start:
                break
            else:
                ret.append(intervals[i])
        newInterval.start = min(intervals[i].start, newInterval.start)
        while i < len(intervals):
            i += 1
            if intervals[i].start <= newInterval.end and intervals[i].end >= newInterval.end:
                break
        newInterval.end = max(intervals[i].end, newInterval.end)
        ret.append(newInterval)
        i += 1
        while i < len(intervals):
            ret.append(intervals[i])
        return ret
"""
