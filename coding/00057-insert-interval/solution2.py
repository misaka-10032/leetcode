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
        Assuming intervals are already sorted according to start

        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        r = []
        phase = 1
        start = newInterval.start
        end = newInterval.end
        for interval in intervals:
            if interval.end < start:
                # stay in phase 1
                r.append(interval)
                continue
            if interval.start > end:
                if phase == 1 or phase == 2:
                    phase = 3
                    r.append(Interval(start, end))
                r.append(interval)
                continue
            if phase == 1:
                phase = 2
                start = min(start, interval.start)
            end = max(end, interval.end)
        if phase == 1 or phase == 2:
            r.append(Interval(start, end))
        return r
