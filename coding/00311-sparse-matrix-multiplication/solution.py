#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import Dict, List


@dataclasses.dataclass
class Point:
    row: int
    col: int
    val: int


class Solution:
    def _build_indexed_points(self, M: List[List[int]], row_based) -> Dict[int, List[Point]]:
        indexed_points = {}
        for row in range(len(M)):
            for col in range(len(M[0])):
                key = row if row_based else col
                val = M[row][col]
                if val:
                    points = indexed_points.get(key, [])
                    points.append(Point(row, col, val))
                    indexed_points[key] = points
        return indexed_points

    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(B[0])
        C = [[0 for _ in range(n)] for _ in range(m)]
        A_col_to_points_map = self._build_indexed_points(A, row_based=False)
        B_row_to_points_map = self._build_indexed_points(B, row_based=True)
        for k, A_points in A_col_to_points_map.items():
            B_points = B_row_to_points_map.get(k, [])
            for B_point in B_points:
                col = B_point.col
                vb = B_point.val
                for A_point in A_points:
                    row = A_point.row
                    va = A_point.val
                    C[row][col] += va * vb
        return C
