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


from collections import Counter


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        ctr = Counter()
        for interval in intervals:
            ctr[interval.start] += 1
            ctr[interval.end] -= 1

        max_cnt = 0
        cnt = 0
        for t in sorted(ctr.keys()):
            cnt += ctr[t]
            max_cnt = max(max_cnt, cnt)
        return max_cnt
