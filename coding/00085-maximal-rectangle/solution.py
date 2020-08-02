#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        # The first 0 on top.
        top = [-1] * n
        # The first col on the left that has less height.
        left = [-1] * n
        # The first col on the right that has less height.
        right = [n] * n

        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    top[j] = i

            # The index of the first 0 on the left.
            leftmost = -1
            for j in range(n):
                if matrix[i][j] == '0':
                    # Reset the left boundary.
                    left[j] = -1
                    leftmost = j
                else:
                    # Potentially update the left boundary due to a 0
                    # on this row.
                    left[j] = max(left[j], leftmost)

            # The index of the first 0 on the right.
            rightmost = n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '0':
                    # Reset the right boundary.
                    right[j] = n
                    rightmost = j
                else:
                    # Potentially update the right boundary due to a 0
                    # on this row.
                    right[j] = min(right[j], rightmost)

            # Find the max area.
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                height = i - top[j]
                width = right[j] - left[j] - 1
                max_area = max(max_area, width * height)

        return max_area
