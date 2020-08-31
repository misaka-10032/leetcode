#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Tuple


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        def _count_lt(target: int) -> Tuple[int, int]:
            i, j = m - 1, 0
            cnt = 0
            max_lt = matrix[0][0]
            while i >= 0 and j < n:
                while i >= 0 and matrix[i][j] >= target:
                    i -= 1
                while j < n and matrix[i][j] < target:
                    cnt += i + 1
                    max_lt = max(max_lt, matrix[i][j])
                    j += 1
            return cnt, max_lt

        lb, ub = matrix[0][0], matrix[m - 1][n - 1]
        while lb < ub:
            target = (lb + ub + 1) // 2
            cnt, max_lt = _count_lt(target)
            if cnt > k:
                # The target is in the upper-left part.
                ub = max_lt
            elif cnt < k:
                # The target is in the lower-right part.
                lb = target
            else:
                return max_lt
        return lb
