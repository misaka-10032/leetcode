#!/usr/bin/env python3
# encoding: utf-8

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if k == 1:
            return matrix[0][0]
        if k == m * n:
            return matrix[-1][-1]

        # Maintain a min heap with the value and the position.
        heap = []
        for i in range(m):
            heap.append((matrix[i][0], i, 0))
        heapq.heapify(heap)

        v = -1
        for _ in range(k):
            v, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return v
