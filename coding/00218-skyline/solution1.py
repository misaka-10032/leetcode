# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        points = []
        for l, r, y in buildings:
            # point is like (x, y)
            points.append([l, y])
            points.append([r, y])

        points = sorted(points)
        # building element is like (l, r, y)
        # heap element is like (-y, r)
        heap, i = [], 0
        for p in points:
            while heap and heap[0][1] <= p[0]:
                heapq.heappop(heap)
            while i < len(buildings) and buildings[i][0] <= p[0]:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1
            if heap:
                p[1] = -heap[0][0]
            else:
                p[1] = 0

        # TODO: can even optimize this into previous loop
        r = [[points[0][0], points[0][1]]]
        for p in points:
            if p[0] == r[-1][0] and p[1] > r[-1][1]:
                r[-1][1] = p[1]
                continue
            if p[1] == r[-1][1]:
                continue
            r.append([p[0], p[1]])

        return r
