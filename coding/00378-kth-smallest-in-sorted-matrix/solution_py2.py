# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* similar to 373
* fix row i's, store candidate j's in pos[i]
* maintain a min heap of (m[i][j], i, j)
* edge case: j >= n  ==> don't push it to heap again
"""

import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0] or not k:
            return -1

        m = len(matrix)
        n = len(matrix[0])
        pos = [0] * m
        heap = []
        for i in xrange(m):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        x = -1
        for _ in xrange(k):
            x, i, j = heapq.heappop(heap)
            j += 1
            pos[i] = j
            if j < n:
                heapq.heappush(heap, (matrix[i][j], i, j))

        return x
