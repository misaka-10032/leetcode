# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import heapq


def dict_acc(d, k):
    if k in d:
        d[k] += 1
    else:
        d[k] = 1


def dict_dec(d, k):
    if k not in d:
        return
    if d[k] == 1:
        d.pop(k)
    else:
        d[k] -= 1


class EdgePoint(object):
    def __init__(self, x, y, left):
        self.x = x
        self.y = y
        self.left = left


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
            left = EdgePoint(l, y, True)
            right = EdgePoint(r, y, False)
            points.append(left)
            points.append(right)

        points = sorted(points, key=lambda p: (p.x, p.y, not p.left))
        heap_neg, y_del = [], {}
        for p in points:
            if p.left:
                heapq.heappush(heap_neg, -p.y)
            else:
                dict_acc(y_del, p.y)
            while heap_neg and -heap_neg[0] in y_del:
                y = -heapq.heappop(heap_neg)
                dict_dec(y_del, y)
            if heap_neg:
                p.y = -heap_neg[0]
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
