#!/usr/bin/env python3
# encoding: utf-8

from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]],
                             B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        intersections = []
        while i < len(A) and j < len(B):
            lb = max(A[i][0], B[j][0])
            ub = min(A[i][1], B[j][1])
            if ub >= lb:
                intersections.append([lb, ub])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return intersections
