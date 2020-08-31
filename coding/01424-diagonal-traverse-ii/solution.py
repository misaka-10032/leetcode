#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = 0
        for row in nums:
            n = max(n, len(row))

        diag_cnt = m + n - 1
        diags = [[] for _ in range(diag_cnt)]
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                diag_idx = i + j
                diags[diag_idx].append(val)

        result = []
        for diag_idx in range(diag_cnt):
            result.extend(reversed(diags[diag_idx]))
        return result
