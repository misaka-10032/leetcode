#!/usr/bin/env python3
# encoding: utf-8

import bisect
from typing import List


class Solution:
    def _find_closest(self, arr: List[int], x: int) -> int:
        i = bisect.bisect_left(arr, x)
        if i > 0 and abs(arr[i - 1] - x) <= abs(arr[i] - x):
            i -= 1
        return i

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = right = self._find_closest(arr, x)
        for _ in range(k - 1):
            left_diff = float('inf')
            if left - 1 >= 0:
                left_cd = arr[left - 1]
                left_diff = abs(left_cd - x)
            right_diff = float('inf')
            if right + 1 < len(arr):
                right_cd = arr[right + 1]
                right_diff = abs(right_cd - x)
            if left_diff <= right_diff:
                left -= 1
            else:
                right += 1
        return arr[left:right + 1]
