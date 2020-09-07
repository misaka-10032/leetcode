#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def _find_pivot(self, digits: List[int]) -> int:
        p = len(digits) - 1
        while p > 0 and digits[p] <= digits[p - 1]:
            p -= 1
        return p

    def nextGreaterElement(self, n: int) -> int:
        digits = [int(c) for c in str(n)]
        # Find the left boundary of a descending sequence on the right.
        p = self._find_pivot(digits)
        if p == 0:
            return -1
        l = len(digits)
        p0 = p - 1
        # Find the last element that is greater than digits[p0].
        while p < l - 1 and digits[p + 1] > digits[p0]:
            p += 1
        digits[p0], digits[p] = digits[p], digits[p0]
        digits[p0 + 1:] = digits[:p0:-1]

        next_int = int(''.join([str(d) for d in digits]))
        max_int = (1 << 31) - 1
        return next_int if next_int < max_int else -1
