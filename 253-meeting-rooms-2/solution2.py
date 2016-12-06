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


import heapq


class Edge(object):
    def __init__(self, t, is_left):
        self.t = t
        self.is_left = is_left


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        edges = []
        l2r = {}
        for interval in intervals:
            left = Edge(interval.start, True)
            right = Edge(interval.end, False)
            edges.append(left)
            edges.append(right)
            l2r[left] = right
        edges = sorted(edges, key=lambda e: (e.t, e.is_left))

        res = 0
        heap = []
        for edge in edges:
            if edge.is_left:
                heapq.heappush(heap, l2r[edge].t)
            else:
                while heap and heap[0] < edge.t:
                    heapq.heappop(heap)
                res = max(res, len(heap))
        return res
