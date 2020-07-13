#!/usr/bin/env python3
# encoding: utf-8

import heapq
from typing import List, Tuple


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # The first element of the tuple is the negative distance square.
        # The second element is the coordinate.
        top_k: List[Tuple[int, List[int]]] = []
        for point in points:
            dist_sq = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(top_k, (-dist_sq, point))
            if len(top_k) > K:
                heapq.heappop(top_k)
        return [t[1] for t in top_k]
