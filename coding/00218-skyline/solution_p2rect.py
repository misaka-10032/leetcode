# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import heapq


class EdgePoint(object):
    def __init__(self, x, y, left):
        self.x = x
        self.y = y
        self.left = left


class Rectangle(object):
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height

    def __cmp__(self, other):
        if -self.height < -other.height:
            return -1
        elif -self.height == -other.height:
            return 0
        else:
            return 1


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        points = []
        l2rect, r2rect = {}, {}
        for l, r, y in buildings:
            left = EdgePoint(l, y, True)
            right = EdgePoint(r, y, False)
            rect = Rectangle(l, r, y)
            l2rect[left] = rect
            r2rect[right] = rect
            points.append(left)
            points.append(right)

        points = sorted(points, key=lambda p: (p.x, p.y, not p.left))
        heap, deleted = [], set()
        for p in points:
            if p.left:
                heapq.heappush(heap, l2rect[p])
            else:
                rect = r2rect[p]
                deleted.add(rect)
            while heap and heap[0] in deleted:
                rect = heapq.heappop(heap)
                deleted.remove(rect)
            if heap:
                p.y = heap[0].height
            else:
                p.y = 0

        r = [[points[0].x, points[0].y]]
        for p in points:
            if p.x == r[-1][0] and p.y > r[-1][1]:
                r[-1][1] = p.y
                continue
            if p.y == r[-1][1]:
                continue
            r.append([p.x, p.y])

        return r
