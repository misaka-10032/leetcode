# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* For each edge, we need to know
  * its x val
  * its height (y)
  * whether it's left or right
* We want to move lower edge up
* Sort each edge by (x, not is_left, height)
  * tricky 1: it's ok to not move up y.prev, as long as x.prev == x.curr,
    because finally we are able to clean them up.
  * tricky 2: but if it's on the right, we don't hurry popping it.
* Maintain a counter mapping height to how many times it appears.
* ctr += 1 when we meet a left edge
* ctr -= 1 when we meet a right edge
* Maintain a heap to record the current highest building.
  * We want max heap, so we push -y
* When ctr goes to 0, remove the element from heap.
  * The trick to remove from heap is delayed remove
  * As we have ctr here, if not ctr[heap[0]], then it should be removed.
  * Don't actually need a remove set, ctr is enough.
* Final trick to merge `edges` to `res`:
  * push the first valid edge
  * later ones compare with the last element of `res`
"""

import heapq
from collections import Counter


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        edges = []
        for xl, xr, y in buildings:
            edges.append([xl, y, True])
            edges.append([xr, y, False])
        edges = sorted(edges, key=lambda e: (e[0], not e[2], e[1]))
        ctr = Counter()  # y's here are normal
        heap = []  # y's here are negated
        for i, (x, y, is_left) in enumerate(edges):
            # push
            if is_left:
                if not ctr[y]:
                    heapq.heappush(heap, -y)
                ctr[y] += 1
            else:
                ctr[y] -= 1

            # pop
            while heap and not ctr[-heap[0]]:
                heapq.heappop(heap)

            # update
            edges[i][1] = -heap[0] if heap else 0

        i = 0
        while i < len(edges)-1 and edges[i+1][0] == edges[i][0]:
            i += 1
        res = [[edges[i][0], edges[i][1]]]
        while i < len(edges):
            while i < len(edges) and edges[i][1] == res[-1][1]:
                i += 1
            while i < len(edges) and edges[i][0] == res[-1][0]:
                i += 1
            res.append([edges[i][0], edges[i][1]])
            i += 1
        return res
