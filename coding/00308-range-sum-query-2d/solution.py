#!/usr/bin/env python3
# encoding: utf-8

import copy
import dataclasses
from typing import List, Optional


@dataclasses.dataclass
class TreeNode:
    # The start index of the row, inclusive.
    row_start: int
    # The end index of the row, exclusive.
    row_end: int
    # The start index of the col, inclusive.
    col_start: int
    # The end index of the col, inclusive.
    col_end: int
    # The sum in the range.
    sum: int = 0
    # The top-left child region.
    top_left: Optional['TreeNode'] = None
    # The top-right child region.
    top_right: Optional['TreeNode'] = None
    # The bottom-left child region.
    bottom_left: Optional['TreeNode'] = None
    # The bottom-right child region.
    bottom_right: Optional['TreeNode'] = None


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self._rows = self._cols = 0
            self._mat = self._root = None
            return
        self._rows, self._cols = len(matrix), len(matrix[0])
        self._mat = copy.deepcopy(matrix)
        self._root = self._build_tree(0, self._rows, 0, self._cols)

    def _build_tree(self, row_start: int, row_end: int,
                    col_start: int, col_end: int) -> TreeNode:
        assert 0 <= row_start < row_end <= self._rows
        assert 0 <= col_start < col_end <= self._cols
        node = TreeNode(row_start, row_end, col_start, col_end)
        if row_start + 1 == row_end and col_start + 1 == col_end:
            node.sum = self._mat[row_start][col_start]
            return node

        row_mid = (row_start + row_end) // 2
        col_mid = (col_start + col_end) // 2
        tot = 0
        if row_start < row_mid:
            if col_start < col_mid:
                node.top_left = self._build_tree(
                    row_start, row_mid, col_start, col_mid)
                tot += node.top_left.sum
            if col_end > col_mid:
                node.top_right = self._build_tree(
                    row_start, row_mid, col_mid, col_end)
                tot += node.top_right.sum
        if row_end > row_mid:
            if col_start < col_mid:
                node.bottom_left = self._build_tree(
                    row_mid, row_end, col_start, col_mid)
                tot += node.bottom_left.sum
            if col_end > col_mid:
                node.bottom_right = self._build_tree(
                    row_mid, row_end, col_mid, col_end)
                tot += node.bottom_right.sum
        node.sum = tot
        return node

    def _update_tree(self, node: Optional[TreeNode], row: int, col: int,
                     delta: int) -> None:
        while node:
            node.sum += delta
            node_row_mid = (node.row_start + node.row_end) // 2
            node_col_mid = (node.col_start + node.col_end) // 2
            if row < node_row_mid:
                if col < node_col_mid:
                    node = node.top_left
                else:
                    node = node.top_right
            else:
                if col < node_col_mid:
                    node = node.bottom_left
                else:
                    node = node.bottom_right

    def update(self, row: int, col: int, val: int) -> None:
        if (row < 0 or row >= self._rows or
                col < 0 or col >= self._cols):
            return
        delta = -self._mat[row][col] + val
        self._mat[row][col] = val
        self._update_tree(self._root, row, col, delta)

    def _sum_range(self, node: TreeNode, row_start: int, row_end: int,
                   col_start: int, col_end: int) -> int:
        assert node.row_start <= row_start < row_end <= node.row_end
        assert node.col_start <= col_start < col_end <= node.col_end
        if (node.row_start == row_start and node.row_end == row_end and
                node.col_start == col_start and node.col_end == col_end):
            return node.sum
        node_row_mid = (node.row_start + node.row_end) // 2
        node_col_mid = (node.col_start + node.col_end) // 2
        tot = 0
        if row_start < node_row_mid:
            if col_start < node_col_mid:
                tot += self._sum_range(
                    node.top_left, row_start, min(node_row_mid, row_end),
                    col_start, min(node_col_mid, col_end))
            if col_end > node_col_mid:
                tot += self._sum_range(
                    node.top_right, row_start, min(node_row_mid, row_end),
                    max(node_col_mid, col_start), col_end)
        if row_end > node_row_mid:
            if col_start < node_col_mid:
                tot += self._sum_range(
                    node.bottom_left, max(node_row_mid, row_start), row_end,
                    col_start, min(node_col_mid, col_end))
            if col_end > node_col_mid:
                tot += self._sum_range(
                    node.bottom_right, max(node_row_mid, row_start), row_end,
                    max(node_col_mid, col_start), col_end)
        return tot

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 = max(0, row1)
        row2 = min(self._rows - 1, row2)
        col1 = max(0, col1)
        col2 = min(self._cols - 1, col2)
        if row1 == row2 and col1 == col2:
            return self._mat[row1][col1]
        return self._sum_range(self._root, row1, row2 + 1, col1, col2 + 1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
