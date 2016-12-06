# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return str((self.start, self.end))


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        n = len(intervals)
        i = 0
        res = []

        # try to find the merge point
        while i < n and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1

        if i == n:
            res.append(newInterval)
            return res

        # 2 possibilities
        # 1. we can merge the intervals
        # 2. the new interval simply skipped
        if intervals[i].start > newInterval.end:
            res.append(newInterval)
        else:
            start = min(intervals[i].start, newInterval.start)
            end = max(intervals[i].end, newInterval.end)
            while i < n and intervals[i].start <= newInterval.end:
                end = max(intervals[i].end, newInterval.end)
                i += 1
            res.append(Interval(start, end))

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
