#!/usr/bin/env python3
# encoding: utf-8

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def _find_first_one(self, mat: 'BinaryMatrix', row: int, cols: int,
                        col_budget: int) -> int:
        left = 0
        right = cols - 1
        # Narrow down the range to row_vals[left:right+1]
        while left < right - 1:
            # Optimization for the budget.
            if left > col_budget:
                return cols
            mid = (left + right) // 2
            val = mat.get(row, mid)
            if val == 1:
                right = mid
            else:
                left = mid + 1
        for col in range(left, right + 1):
            if mat.get(row, col):
                return col
        # Not found :-(
        return cols

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        min_col = cols
        for row in range(rows):
            col = self._find_first_one(binaryMatrix, row, cols, min_col)
            min_col = min(min_col, col)
        return min_col if min_col < cols else -1
