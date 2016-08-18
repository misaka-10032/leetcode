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
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        r = []
        intervals = sorted(intervals, key=lambda x: x.start)
        start = intervals[0].start
        end = intervals[0].end
        i = 1
        while i < len(intervals):
            if intervals[i].start > end:
                # new interval
                r.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
            elif intervals[i].end > end:
                # merge
                end = intervals[i].end
            i += 1
        r.append(Interval(start, end))
        return r
